import Head from "next/head";
import styles from "../styles/Home.module.css";
import Image from "next/image";
import { Carousel } from "react-responsive-carousel";
import "react-responsive-carousel/lib/styles/carousel.min.css"; // requires a loader

export default function Home() {
  return (
    <>
      <div>
        <main className="flex flex-col h-auto md:h-screen lg:h-screen justify-center text-center bg-gray-50 p-5 md:p-24 lg:pt-24 ">
          <div className="text-8xl font-thin mb-5 mx-auto">
            <h1
              className={
                "bg-clip-text text-transparent bg-gradient-to-r from-green-400 to-blue-500 "
              }
            >
              EgyBest Spider V4.0
            </h1>
          </div>
          <h3
            className={
              "text-3xl text-gray-700 mb-2 mx-auto w-auto md:w-1/2 lg:w-1/2"
            }
          >
            برنامج يُمكنك من تخطي الاعلانات المزعجه في موقع ايجي بيست تسطيع من
            خلاله الحصول علي لينكات التحميل المباشره لأي مسلسل
          </h3>
          <div className={"flex flex-row justify-center"}>
            <div className="bg-red-700 text-white px-2 rounded-full mx-2">
              <h1>V4.0</h1>
            </div>
            <div className="bg-green-800 text-white px-2 rounded-full">
              <h1>No Current Problems Detected</h1>
            </div>
          </div>

          <div className="w-auto mx-auto mt-9">
            <Carousel autoPlay={true} swipeable={true}>
              <div>
                <Image
                  src="/carousal/1.jpg"
                  width={400}
                  height={300}
                  alt="واجه برنامج ايجي بيست سبايدر"
                />
              </div>
              <div>
                <Image
                  src="/carousal/2.jpg"
                  width={400}
                  height={300}
                  alt="واجه برنامج ايجي بيست سبايدر"
                />
              </div>
            </Carousel>
            <div
              onClick={() =>
                window.open(
                  "https://nchub.s3.amazonaws.com/EgyBest+Spider+V4.0.rar",
                  "_blank"
                )
              }
              className="bg-blue-800 text-white rounded-full p-2 flex-row flex cursor-pointer justify-center w-40 mx-auto"
            >
              <h1 className="mt-1 ml-2 ">حمل الان</h1>
              <Image
                src="/download.png"
                className="mr-2"
                width={32}
                height={32}
                alt="تحميل"
              />
            </div>
          </div>
        </main>

        <footer className={styles.footer}>
          <a
            href="https://nasrika.com"
            target="_blank"
            rel="noopener noreferrer"
            className="text-2xl font-light"
          >
            Developed with 💝 By:{" "}
            <img
              src="/logo.png"
              alt="Mahmoud Nasr Logo"
              className={styles.logo}
            />
          </a>
        </footer>
      </div>
    </>
  );
}
