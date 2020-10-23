const BASE_LINK = "https://nspider.herokuapp.com/";

function get_current_tab_url() {
  return new Promise((resolve, reject) => {
    chrome.tabs.query(
      {
        active: true,
        lastFocusedWindow: true,
      },
      (tabs) => {
        var tab = tabs[0];
        var tab_url = tab.url;
        resolve(tab_url);
      }
    );
  });
}
function get_cookies(domain, name) {
  return new Promise((resolve, reject) => {
    chrome.cookies.get(
      {
        url: domain,
        name: name,
      },
      function (res) {
        if (res) {
          resolve(res.value);
        }
      }
    );
  });
}
async function get_episodes_links(url) {
  return new Promise(async (resolve, reject) => {
    const req_episodes = await fetch(url, {
      method: "GET",
    });
    const episodes = await req_episodes.text();

    const parser = new DOMParser();
    const htmlDocument = parser.parseFromString(episodes, "text/html");
    var element = htmlDocument.documentElement.querySelectorAll(
      ".movies_small a[href]"
    );
    const episodes_links = [];
    element.forEach((i) => {
      if (i.href.includes("/episode/")) {
        episodes_links.push(i.href);
      }
    });
    resolve(episodes_links);
  });
}

async function get_download_links(urls) {
  return new Promise(async (resolve, reject) => {
    download_links = [];
    for (var i = 0; i < urls.length; i++) {
      const res_api = await fetch(urls[i], {
        method: "GET",
        headers: {
          "user-agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        },
      });
      if (res_api.status == 200) {
        const res_text = await res_api.text();

        const parser = new DOMParser();
        const htmlDocument = parser.parseFromString(res_text, "text/html");
        var element = htmlDocument.documentElement.querySelector(
          "._open_window"
        );
        download_link = element["dataset"]["url"];
        download_links.push(download_link);
      } else {
        go3_unavailable.push(e);
      }
    }
    resolve(download_links);
  });
}

async function go_to_video_stream(api_links, current_domain) {
  return new Promise(async (resolve, reject) => {
    const domain = "https://" + current_domain.split("/")[2];
    const cookie = await get_cookies(domain, "PSSID");
    const vsl = [];
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    for (let index = 0; index < api_links.length; index++) {
      const element = api_links[index];

      var raw = JSON.stringify({
        url: element,
        cookie: "PSSID=" + cookie,
      });
      var requestOptions = {
        method: "POST",
        headers: myHeaders,
        body: raw,
        redirect: "follow",
      };
      const video_stream_link = await fetch(BASE_LINK, requestOptions);
      const json_vsl = await video_stream_link.json();
      vsl.push(json_vsl.url);
    }
    resolve(vsl);
  });
}

async function get_direct_links(video_streams_links) {
  return new Promise(async (resolve, rejected) => {
    let broken_direct = {};
    broken_direct.direct = [];
    broken_direct.broken = [];
    for (let i = 0; i < video_streams_links.length; i++) {
      var myHeaders = new Headers();
      myHeaders.append("Content-Type", "application/json");
      const element = video_streams_links[i];
      const domain = "https://" + element.split("/")[2];
      const cookie = await get_cookies(domain, "PHPSID");
      const path = element.split("/")[4];
      const raw = JSON.stringify({
        cookie: "PHPSID=" + cookie,
        domain: domain,
        path: "/f/" + path,
      });
      var requestOptions = {
        method: "POST",
        body: raw,
        headers: myHeaders,
      };
      const direct_link_dom = await fetch(`${BASE_LINK}d`, requestOptions);
      const dom_text = await direct_link_dom.text();
      const parser = new DOMParser();
      const htmlDocument = parser.parseFromString(dom_text, "text/html");
      var query_element = htmlDocument.documentElement.querySelectorAll(
        ".bigbutton"
      );

      if (query_element[0].href) {
        broken_direct.direct.push(query_element[0].href);
      } else {
        broken_direct.broken.push(element);
      }
    }
    resolve(broken_direct);
  });
}

async function handle_broken(broken_direct) {
  return new Promise((resolve, reject) => {
    const { broken } = broken_direct;
    const done_domains = [];
    for (let i = 0; i < broken.length; i++) {
      const element = broken[i];

      let sub_domain = element.split("/")[2];

      const is_done = done_domains.find((e) => e === sub_domain);
      if (!is_done) {
        chrome.tabs.create(
          {
            url: element,
            active: false,
          },
          function (tab) {
            console.log(tab);

            setTimeout(() => {
              chrome.tabs.remove(tab.id);
            }, 5000);
          }
        );
        setTimeout(() => {}, 2000);
        done_domains.push(sub_domain);
      }
    }
    resolve("");
  });
}
function save_links(arrLinks, name) {
  var textDoc = document.createElement("a");

  textDoc.href = "data:attachment/text," + encodeURI(arrLinks.join("\n"));
  textDoc.target = "_blank";
  textDoc.download = name + ".txt";
  textDoc.click();
}
async function start() {
  const current_url = await get_current_tab_url();

  const episode_links = await get_episodes_links(current_url);

  const download_links = await get_download_links(episode_links);

  const video_stream = await go_to_video_stream(download_links, current_url);

  const direct_links = await get_direct_links(video_stream);

  const season_name = current_url.split("season/")[1].replace("/", "");
  let final_links = [];

  if (direct_links.broken) {
    await handle_broken(direct_links);
    const get_direct_broken = await get_direct_links(direct_links.broken);
    final_links = [...direct_links.direct, get_direct_broken.direct];
  } else {
    final_links = direct_links.direct;
  }
  console.log(final_links);
  save_links(final_links, season_name);
}
chrome.contextMenus.create({
  title: "Get Season Download Links",
  contexts: ["all"],
  onclick: start,
  documentUrlPatterns: ["*://*.egybest.com/season/*"],
});
