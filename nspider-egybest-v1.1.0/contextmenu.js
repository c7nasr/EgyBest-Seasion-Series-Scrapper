const _0x27ab=['Wrong\x20Value','Chrome\x20Error.\x20Just\x20Refresh\x20the\x20Page\x20and\x20Try\x20again','querySelectorAll','Cookie','url','follow','broken','contextMenus','replace','parseFromString','cookies','length','PSSID','POST','/episode/','.movies_small\x20a[href]','tabs','push','/f/','get','PHPSID=','querySelector','log','split','documentElement','append','application/json','text/html','download','text','create','query','Content-Type','href','click','Get\x20Season\x20Download\x20Links','value','target','stringify','PHPSID','GET','join','https://','direct','status','.txt','all'];(function(_0x40ff28,_0x27ab39){const _0x3e9dbb=function(_0x3b2ee1){while(--_0x3b2ee1){_0x40ff28['push'](_0x40ff28['shift']());}};_0x3e9dbb(++_0x27ab39);}(_0x27ab,0xcb));const _0x3e9d=function(_0x40ff28,_0x27ab39){_0x40ff28=_0x40ff28-0x0;let _0x3e9dbb=_0x27ab[_0x40ff28];return _0x3e9dbb;};const _0x414e0d=_0x3e9d;function get_current_tab_url(){return new Promise((_0x3b2ee1,_0x29bdfd)=>{const _0x5b16e4=_0x3e9d;chrome['tabs'][_0x5b16e4('0x10')]({'active':!![],'lastFocusedWindow':!![]},_0x4340b1=>{const _0x248518=_0x5b16e4;_0x4340b1[_0x248518('0x2b')]===0x0&&(alert(_0x248518('0x21')),_0x29bdfd(_0x248518('0x21')));var _0x217d1c=_0x4340b1[0x0],_0x4a4d1e=_0x217d1c[_0x248518('0x24')];_0x3b2ee1(_0x4a4d1e);});});}function get_cookies(_0x2f6971,_0x4caf22){return new Promise((_0x536df1,_0x49cb81)=>{const _0x453d32=_0x3e9d;chrome[_0x453d32('0x2a')][_0x453d32('0x4')]({'url':_0x2f6971,'name':_0x4caf22},function(_0x969d63){const _0x445460=_0x453d32;_0x969d63?_0x536df1(_0x969d63[_0x445460('0x15')]):_0x536df1(_0x445460('0x20'));});});}async function get_episodes_links(_0x3316a5){return new Promise(async(_0x136a5d,_0x477515)=>{const _0x245a17=_0x3e9d,_0x5ef006=await fetch(_0x3316a5,{'method':_0x245a17('0x19')}),_0x51a19d=await _0x5ef006[_0x245a17('0xe')](),_0xa0a0b=new DOMParser(),_0x5222bf=_0xa0a0b[_0x245a17('0x29')](_0x51a19d,_0x245a17('0xc'));var _0x851e8f=_0x5222bf[_0x245a17('0x9')][_0x245a17('0x22')](_0x245a17('0x0'));const _0x16abab=[];_0x851e8f['forEach'](_0x21bbb4=>{const _0x51fe56=_0x245a17;_0x21bbb4['href']['includes'](_0x51fe56('0x2e'))&&_0x16abab[_0x51fe56('0x2')](_0x21bbb4[_0x51fe56('0x12')]);}),_0x136a5d(_0x16abab);});}async function get_download_links(_0x23cfd7){return new Promise(async(_0x8b0a91,_0x498c8f)=>{const _0x422d89=_0x3e9d;download_links=[];for(var _0xb22cc0=0x0;_0xb22cc0<_0x23cfd7['length'];_0xb22cc0++){const _0x51be34=await fetch(_0x23cfd7[_0xb22cc0],{'method':_0x422d89('0x19'),'headers':{'user-agent':'Mozilla/5.0\x20(Windows\x20NT\x2010.0;\x20Win64;\x20x64)\x20AppleWebKit/537.36\x20(KHTML,\x20like\x20Gecko)\x20Chrome/86.0.4240.111\x20Safari/537.36'}});if(_0x51be34[_0x422d89('0x1d')]==0xc8){const _0x3624f1=await _0x51be34['text'](),_0x744192=new DOMParser(),_0x2f1ddb=_0x744192[_0x422d89('0x29')](_0x3624f1,_0x422d89('0xc'));var _0x7fd7c5=_0x2f1ddb['documentElement'][_0x422d89('0x6')]('._open_window');download_link=_0x7fd7c5['dataset'][_0x422d89('0x24')],download_links[_0x422d89('0x2')](download_link);}else go3_unavailable[_0x422d89('0x2')](e);}_0x8b0a91(download_links);});}async function go_to_video_stream(_0xe0aab6,_0x457b81){return new Promise(async(_0x2468f7,_0x403b96)=>{const _0x3e25b4=_0x3e9d,_0x167536=_0x3e25b4('0x1b')+_0x457b81[_0x3e25b4('0x8')]('/')[0x2],_0x58f350=await get_cookies(_0x167536,_0x3e25b4('0x2c')),_0x56d6e1=[];console[_0x3e25b4('0x7')](_0x167536);for(let _0x564223=0x0;_0x564223<_0xe0aab6[_0x3e25b4('0x2b')];_0x564223++){try{const _0x9aa8a4=_0xe0aab6[_0x564223];var _0x26cac7=new Headers();_0x26cac7[_0x3e25b4('0xa')](_0x3e25b4('0x11'),_0x3e25b4('0xb')),_0x26cac7[_0x3e25b4('0xa')](_0x3e25b4('0x23'),'PSSID='+_0x58f350);var _0x4cc4ed={'method':_0x3e25b4('0x2d'),'headers':_0x26cac7,'redirect':_0x3e25b4('0x25')};const _0x16c982=await fetch(_0x167536+_0x9aa8a4,_0x4cc4ed);_0x56d6e1[_0x3e25b4('0x2')](_0x16c982[_0x3e25b4('0x24')]);}catch(_0x34e4f3){console[_0x3e25b4('0x7')](_0x34e4f3);continue;}}_0x2468f7(_0x56d6e1);});}async function get_direct_links(_0x560bc9){var _0x21a767=_0x560bc9;return console['log'](_0x21a767),new Promise(async(_0x12124b,_0x2fa41f)=>{const _0x597651=_0x3e9d;let _0x37e82e={};_0x37e82e['direct']=[],_0x37e82e[_0x597651('0x26')]=[];var _0x249f2f=new Headers();_0x249f2f[_0x597651('0xa')](_0x597651('0x11'),_0x597651('0xb'));for(let _0x248128=0x0;_0x248128<_0x560bc9[_0x597651('0x2b')];_0x248128++){const _0x3b9976=_0x560bc9[_0x248128];console[_0x597651('0x7')](_0x3b9976);const _0x412be4='https://'+_0x3b9976['split']('/')[0x2],_0xed1da9=await get_cookies(_0x412be4,_0x597651('0x18')),_0x31e5fd=_0x3b9976[_0x597651('0x8')]('/')[0x4],_0x5867e0=JSON[_0x597651('0x17')]({'cookie':_0x597651('0x5')+_0xed1da9,'domain':_0x412be4,'path':_0x597651('0x3')+_0x31e5fd});var _0x2a4313={'method':'POST','body':_0x5867e0,'headers':_0x249f2f};const _0x2ffde6=await fetch(_0x3b9976,_0x2a4313),_0x256a19=await _0x2ffde6[_0x597651('0xe')](),_0x5bd6ef=new DOMParser(),_0x1d2d01=_0x5bd6ef[_0x597651('0x29')](_0x256a19,_0x597651('0xc'));var _0x523dcf=_0x1d2d01[_0x597651('0x9')][_0x597651('0x22')]('.bigbutton');console['log'](_0x523dcf[0x0][_0x597651('0x12')]),_0x523dcf[0x0][_0x597651('0x12')]?_0x37e82e[_0x597651('0x1c')][_0x597651('0x2')](_0x523dcf[0x0]['href']):_0x37e82e[_0x597651('0x26')][_0x597651('0x2')](_0x3b9976);}_0x12124b(_0x37e82e);});}async function handle_broken(_0x2266e7){return new Promise((_0xc62f0d,_0x817100)=>{const _0x1a2cbc=_0x3e9d,{broken:_0x2d75b9}=_0x2266e7,_0x5b057d=[];for(let _0x1896a3=0x0;_0x1896a3<_0x2d75b9['length'];_0x1896a3++){const _0x45a01c=_0x2d75b9[_0x1896a3];let _0x4b3e5c=_0x45a01c[_0x1a2cbc('0x8')]('/')[0x2];const _0x350d7a=_0x5b057d['find'](_0x42a80d=>_0x42a80d===_0x4b3e5c);!_0x350d7a&&(chrome[_0x1a2cbc('0x1')][_0x1a2cbc('0xf')]({'url':_0x45a01c,'active':![]},function(_0x515f69){console['log'](_0x515f69),setTimeout(()=>{chrome['tabs']['remove'](_0x515f69['id']);},0x1388);}),setTimeout(()=>{},0x7d0),_0x5b057d['push'](_0x4b3e5c));}_0xc62f0d('');});}function save_links(_0x29ea47,_0x1fc429){const _0x2edc63=_0x3e9d;var _0x72357d=document['createElement']('a');_0x72357d[_0x2edc63('0x12')]='data:attachment/text,'+encodeURI(_0x29ea47[_0x2edc63('0x1a')]('\x0a')),_0x72357d[_0x2edc63('0x16')]='_blank',_0x72357d[_0x2edc63('0xd')]=_0x1fc429+_0x2edc63('0x1e'),_0x72357d[_0x2edc63('0x13')]();}async function start(){const _0x588b71=_0x3e9d,_0x29f848=await get_current_tab_url(),_0x43029a=_0x29f848[_0x588b71('0x8')]('season/')[0x1][_0x588b71('0x28')]('/',''),_0x26b52e=await get_episodes_links(_0x29f848),_0x493220=await get_download_links(_0x26b52e),_0x1d1f4e=await go_to_video_stream(_0x493220,_0x29f848),_0x4326f8=await get_direct_links(_0x1d1f4e);let _0x5c466f=[];if(_0x4326f8[_0x588b71('0x26')]){await handle_broken(_0x4326f8);const _0x130974=await get_direct_links(_0x4326f8[_0x588b71('0x26')]);_0x5c466f=[..._0x4326f8[_0x588b71('0x1c')],_0x130974['direct']];}else _0x5c466f=_0x4326f8[_0x588b71('0x1c')];console[_0x588b71('0x7')](_0x5c466f),save_links(_0x5c466f,_0x43029a);}chrome[_0x414e0d('0x27')]['create']({'title':_0x414e0d('0x14'),'contexts':[_0x414e0d('0x1f')],'onclick':start,'documentUrlPatterns':['*://*.egybest.com/season/*']});