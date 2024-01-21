import React from "react";
import {RiTwitterLine} from "react-icons/ri";
import {AiFillGithub} from "react-icons/ai";

export default function Header() {

	return (<header className="fixed top-0 z-50 w-full clearNav">
		<div className="flex flex-col flex-wrap items-center max-w-5xl p-5 mx-auto md:flex-row">
			<div className="flex flex-row items-center justify-center p-3 md:p-1">
				<a
					href="/"
					className="flex mb-4 text-3xl font-medium text-white md:mb-0"
				>
					<img
						src={"/logo.png"}
						className={"w-16 rounded-full"} alt={"EgyBest Downloader Logo"}/>
				</a>

			</div>

			<div
				className={"flex-grow items-center justify-center md:justify-end hidden sm:flex sm:gap-4"}
			>
				<a
					href="https://twitter.com/sgitnasr"
					rel="noopener noreferrer"
					target="_blank"
				>
					<RiTwitterLine className={"fill-white"} size={32}/>
				</a>
				<a
					href="https://github.com/gitnasr/EgyBest-Downloader"
					rel="noopener noreferrer"
					target="_blank"
				>
					<AiFillGithub size={32} color={"white"}/>
				</a>
			</div>
		</div>
	</header>);
}