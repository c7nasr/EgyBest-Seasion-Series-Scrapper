import HowToUse from "./Video";
import Image from "next/image";

export default function Main() {
  return (
    <section className="text-gray-600 body-font">
      <div className="max-w-5xl mx-auto pt-52 pb-14">
        <h1 className="mb-6 text-5xl font-bold text-center text-white px-7 sm:text-8xl font-4 lh-6 ld-04 ">
          برنامج التحميل بدون اعلانات من ايجي بيست
        </h1>
        <h2 className="pb-5 text-2xl font-semibold text-center text-gray-700 px-7 font-4 lh-6 ld-04">
           حمل من ايجي بيست بدون اعلانات تقدر تحمل السيزون كله او المسلسل كله
          <br />
          وتختار الكوالتي كمان بضغط زرار
        </h2>
    <div className={"flex items-center min-w-full mx-auto flex-col gap-3 sm:flex-row-reverse flex-wrap justify-center"}>
      <a href="https://github.com/gitnasr/EgyBest-Downloader/releases/latest" target="_blank" className="flex flex-col justify-center w-3/4 py-3 text-lg text-white bg-blue-600 rounded-md cursor-pointer px-14 sm:w-1/2 hover:bg-blue-700">
        <span className="text-3xl font-extrabold text-center">تحميل</span>
        <span className="text-xs text-center">الاصدار الحالي: 6.1</span>
      </a>
      <div className={"flex flex-row gap-x-3 gap-y-2 mr-3 items-center"}>

        <h3 className="px-3 py-3 text-center text-cyan-700">
          البرنامج أمن ومجاني، ربما تقوم بعض مضادات الفيروسات بتصنيف البرنامج كفيروس بالخطأ
        </h3>
    </div>

      </div>
      </div>

      <div className="container flex flex-col items-center justify-center mx-auto">
            <Image
            className="object-contain object-center w-full px-3 mb-10 rounded-lg shadow-md sm:px-0 sm:w-1/2 "
            alt="EgyBest Downloader"
            src="/screenshot.png"
            width={720}
            height={500}
        />
      </div>
      <h2 className="mb-1 text-4xl font-semibold tracking-tighter text-center text-gray-200 pt-14 lg:text-7xl md:text-6xl">
        أسهل طريقة استخدام
      </h2>
      <br></br>
      <p className="mx-auto text-xl font-normal leading-relaxed text-center text-gray-300 fs521 lg:w-2/3">
        تم تصميم البرنامج ليكون سهل الاستخدام حيث تستيطع ببضع خطوات الحصول علي لينكات التحميل المباشره لآي مسلسل او سيزون علي ايجي بيست
      </p>
      <div dir={"rtl"} className="max-w-4xl px-3 pt-12 pb-24 mx-auto fsac4 md:px-1">
        <div className="ktq4">
          <h1 className={"w-10 font-extrabold text-4xl"}>1</h1>
          <h3 className="pt-3 text-lg font-semibold text-white">
            حدد السيزون أو المسلسل اللي عايز تحمله
          </h3>
          <p className="pt-2 text-gray-200 value-text text-md fkrr1">
            هتروح علي ايجي بيست (اي دومين فيهم) وتختار المسلسل او السيزون اللي عايز تحملة وتعمل للينك كوبي اهم حاجة تتأكد انه لينك السيزون او المسلسل مش لينك حلقة
          </p>
        </div>
        <div className="ktq4">
          <h1 className={"w-10 font-extrabold text-4xl"}>2</h1>
          <h3 className="pt-3 text-lg font-semibold text-white">
            هتروح علي البرنامج وتختار الجودة المطلوبة
          </h3>
          <p className="pt-2 text-gray-200 value-text text-md fkrr1">
            البرنامج بيسمحلك إنك تختار الجودة اللي انت عايزها عشان تحافظ علي باقة النت، من اول 1080p لحد 360p. بعد ما تختار وتعمل باست للينك في البرنامج دوس استارت
          </p>
        </div>
        <div className="ktq4">
          <h1 className={"w-10 font-extrabold text-4xl"}>3</h1>
          <h3 className="pt-3 text-lg font-semibold text-white">
            البرنامج هيبدأ في استخلاص اللينكات
          </h3>
          <p className="pt-2 text-gray-200 value-text text-md fkrr1">
            بعد ما تدوس ستارت البرنامج هيبدأ يقوم بشغله انه يجيبلك اللينكات المباشره للتحميل لكل الحلقات سواء للسيزون او للمسلسل كله بالجودة اللي انت حددتها
          </p>
        </div>
        <div className="ktq4">
          <h6 className={"w-10 font-extrabold text-4xl"}>4</h6>
          <h3 className="pt-3 text-lg font-semibold text-white">
            اللينكات جاهزة للداونلود
          </h3>
          <p className="pt-2 text-gray-200 value-text text-md fkrr1">
            بعد ما البرنامج ما يخلص، هتلاقي ملف تيكست بأسم السيزون او المسلسل الملف ده هيكون فيه لينكات التحميل المباشرة للحلقات، تقدر تاخدها وتحطها علي اي برنامج تحميل سواء كمبيوتر او موبايل
          </p>
        </div>
      </div>
      <div className="flex justify-center max-w-6xl px-3 mx-auto pt-7 md:px-4">
        <HowToUse/>
      </div>

    </section>
  );
}