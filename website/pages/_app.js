import Head from "next/head";

import "../styles/globals.css";

function MyApp({ Component, pageProps }) {
  return (
    <>
      <Head>
        <title>EgyBest Spider</title>
        <link rel="icon" href="/favicon.ico" />
        <meta
          name="description"
          content="برنامج يمكنك من تخطي الاعلانات المزعجه في موقع ايجي بيست تسطيع من خلاله الحصول علي لينكات التحميل المباشره لأي مسلسل لتحميله مره واحده"
        />
        <meta property="og:title" content="EgyBest Spider V4.0" />
        <meta
          property="og:description"
          content="برنامج يمكنك من تخطي الاعلانات المزعجه في موقع ايجي بيست تسطيع من خلاله الحصول علي لينكات التحميل المباشره لأي مسلسل لتحميله مره واحده"
        />
        <meta property="og:url" content="https://eb.nasrika.com" />
        <meta property="og:type" content="website" />
        <meta property="og:locale" content="ar_EG" />
        <meta
          name="google-site-verification"
          content="XiY4d8aeyWuF36G8yOoV5HKDZ-eOpTwbAJS1lpSqZZA"
        />
        <meta property="og:image" content="/og.png" />

        <link rel="canonical" href="https://eb.nasrika.com/" />

        <meta name="robots" content="index, follow" />
      </Head>

      <Component {...pageProps} />
    </>
  );
}

export default MyApp;
