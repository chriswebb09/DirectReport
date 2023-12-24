
const { useState, useEffect } = React;

const AccountUserInfo = (userData, reportData) => {
    return (
        <div className="lg:col-span-3 md:col-span-2 sm:col-span-1 sm:col-span-3 justify-center">
            <div className="bg-blue-500 py-6 px-10 my-2 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl">
                <div className="flex h-30 flex-col self-center bg-blue-200 py-8 px-2 my-6 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl border-solid border-2 border-gray-200">
                    <div className="lg:col-span-1 md:col-span-2 sm:col-span-3 mx-10 pb-8 pt-8 px-8 bg-blue-50 rounded-t-3xl shadow-[1.0px_1.0px_7.0px_0.0px_rgba(0,0,0,0.58)] border-solid border-2 border-gray-200">
                        <div className="grid grid-flow-col gap-8">
                            <div className="col-span-2 bg-gray-200 shadow-[1.0px_1.0px_7.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl py-8 px-5 border-solid border-2 border-gray-400">
                                <p className="text-justify ml-5 pt-1 text-md font-mono tracking-wide text-sky-800">
                                    <span className="ml-2 font-black">FULL NAME:  </span> {userData.name}
                                </p>
                                <p className="text-justify ml-5 pt-1 text-md font-mono tracking-wide text-sky-800">
                                        <span className="ml-2 font-black font-mono">EMAIL ADDRESS:</span> {userData.userid}
                                </p>
                                <p className="text-justify ml-5 pt-1 text-md font-mono tracking-wide text-sky-800">
                                        <span className="ml-2 font-black font-mono">USER NAME:  </span> {userData.username}
                                </p>
                                <div className=" rounded-2xl flex items-center justify-center">
                                    <button
                                        className="bg-sky-500 hover:bg-slate-100 self-center text-white font-mono tracking-wide shadow-[1.5px_2px_1.0px_0.5px_rgba(0,0,0,0.48)] hover:white hover:text-blue-500 hover:border-gray-200 text-md font-semibold py-2 px-30 rounded-3xl mt-5"
                                        type="button">
                                        <a className="px-10 py-2 tracking-wide"
                                           href='/authorize/github'>EDIT PROFILE</a>
                                    </button>
                                </div>
                            </div>
                            <div className="col-span-2 bg-gray-200 shadow-[1.0px_1.0px_7.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl py-8 px-5 border-solid border-2 border-gray-400">
                                <p className="text-justify ml-5 pt-1 text-md font-mono tracking-wide text-sky-800">
                                    <span className="ml-2 font-black font-mono">NUMBER OF REPORTS SAVED:  </span> {reportData.length}
                                </p>
                                <p className="text-justify ml-5  pt-1 text-md font-mono tracking-wide text-sky-800">
                                    <span className="ml-2 font-black font-mono">LAST REPORT:  </span> DEC
                                    12, 2021
                                </p>
                                <p className="text-justify ml-5 pt-1 text-md font-mono tracking-wide text-sky-800">
                                    <span className="ml-2 font-black font-mono">SELECTED REPO:  </span> DirectReport
                                </p>
                                <div className=" rounded-2xl flex items-center justify-center">
                                    <button
                                        className="bg-sky-500 hover:bg-slate-100 self-center text-white font-mono tracking-wide shadow-[1.5px_2px_1.0px_0.5px_rgba(0,0,0,0.48)] hover:white hover:text-blue-500 hover:border-gray-200 text-md font-semibold py-2 px-30 rounded-3xl mt-5"
                                        type="button">
                                        <a className="px-10 py-2 tracking-wide"
                                           href='/authorize/github'>NEW REPORT</a>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="lg:col-span-1 md:col-span-2 sm:col-span-3 mx-10 lg:px-18 md:px-4 sm:px-0 bg-gray-200 shadow-[1.0px_1.0px_7.0px_0.0px_rgba(0,0,0,0.58)] rounded-b-3xl shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)] ">
                        <div className="rounded-2xl flex items-center justify-center">
                            <h3 className="self-center text-center pt-5 text-sky-800 tracking-wide text-lg text-center font-black font-mono pb-3">CONNECT GITHUB ACCOUNT</h3>
                        </div>
                        <div className="rounded-2xl flex items-center justify-center">
                            <button className="bg-sky-500 hover:bg-slate-100 self-center text-white font-mono tracking-wide shadow-[1.5px_2px_1.0px_0.7px_rgba(0,0,0,0.48)] hover:white hover:text-blue-500 hover:border-gray-200 text-lg font-semibold py-2 px-10 rounded-3xl mt-1 mb-8" type="button">
                                <a className="px-10 py-2 tracking-wide" href='/authorize/github'>AUTHORIZE CONNECTION</a>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}