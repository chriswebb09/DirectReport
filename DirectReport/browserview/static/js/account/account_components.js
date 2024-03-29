
const { useState, useEffect } = React;

const AccountUserInfo = (userData, reportData) => {
    return (
        <div className="lg:col-span-3 md:col-span-2 my-2 sm:col-span-1 sm:col-span-3 justify-center px-20 mx-10">
            <div className="bg-blue-600 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl mx-22 px-2 py-1">
                <div className="flex h-30 flex-col self-center py-10 px-5 my-3 rounded-3xl">
                    <div className="lg:col-span-1 md:col-span-2 sm:col-span-3 mx-5 pb-8 pt-12 px-10 bg-blue-50 rounded-t-3xl shadow-[1.0px_1.0px_7.0px_0.0px_rgba(0,0,0,0.58)] border-solid border-2 border-gray-200">
                        <div className="grid grid-flow-col gap-10">
                            <div className="col-span-2 bg-gray-200 shadow-[1.0px_1.0px_7.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl py-7 border-solid border-2 border-gray-400">
                                <p className="text-left ml-7 pt-1 text-md font-mono tracking-wide text-sky-800">
                                    <span className="font-black mr-5 text-right">FULL NAME:  </span> <span className="text-right">{userData.name}</span>
                                </p>
                                <p className="text-left ml-7 pt-1 text-md font-mono tracking-wide text-sky-800">
                                    <span className="font-black font-mono mr-5 text-right">EMAIL ADDRESS:</span> <span className="text-right">{userData.userid}</span>
                                </p>
                                <p className="text-left ml-7 pt-1 text-md font-mono tracking-wide text-sky-800">
                                    <span className="font-black font-mono mr-5 text-right">USER NAME:  </span> <span className="text-right">{userData.username}</span>
                                </p>
                                <div className="rounded-2xl flex items-center justify-center">
                                    <button className="bg-blue-600 hover:bg-slate-100 self-center text-white font-mono tracking-wide shadow-[1.5px_2px_1.0px_0.5px_rgba(0,0,0,0.48)] hover:white hover:text-blue-500 hover:border-gray-200 text-sm font-semibold py-2 px-30 rounded-3xl mt-5" type="button">
                                        <a className="px-20 py-2 tracking-wide" href='/dashboard/edit'>EDIT PROFILE</a>
                                    </button>
                                </div>
                            </div>
                            <div className="col-span-2 bg-gray-200 shadow-[1.0px_1.0px_7.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl py-7 border-solid border-2 border-gray-400">
                                <p className="text-justify ml-7 pt-1 text-md font-mono tracking-wide text-sky-800">
                                    <span className="font-black font-mono">NUMBER OF REPORTS SAVED:  </span>
                                    {reportData.length}
                                </p>
                                <p className="text-justify ml-7 pt-1 text-md font-mono tracking-wide text-sky-800">
                                    <span className="font-black font-mono">DATE STARTED TRACKING:  </span>
                                    DEC 12, 2018
                                </p>
                                <p className="text-justify ml-7 pt-1 text-md font-mono tracking-wide text-sky-800">
                                    <span className="font-black font-mono">LAST REPORT CREATED:  </span>
                                    DEC 12, 2021
                                </p>

                                <div className=" rounded-2xl flex items-center justify-center">
                                    <button className="bg-blue-600 hover:bg-slate-100 self-center text-white font-mono tracking-wide text-sm font-semibold shadow-[1.5px_2px_1.0px_0.5px_rgba(0,0,0,0.48)] hover:white hover:text-blue-500 hover:border-gray-200 py-2 px-30 rounded-3xl mt-5"
                                        type="button">
                                        <a className="px-20 py-2 tracking-wide" href='/dashboard/reports/new'>NEW REPORT</a>
                                    </button>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="lg:col-span-1 md:col-span-2 sm:col-span-3 mx-5 lg:px-18 md:px-4 sm:px-0 bg-gray-200 shadow-[1.0px_1.0px_7.0px_0.0px_rgba(0,0,0,0.58)] rounded-b-3xl shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)] ">
                        <div className="mx-0 min-w-full flex flex-col items-center">
                            <h1 className="mx-10 pt-6 font-black font-mono tracking-wide text-xl text-sky-800">
                                CONNECT ACCOUNT
                            </h1>
                        </div>
                        <div className="flex items-center justify-center py-1">
                           <ul>
                               <li>
                                   <p className="text-justify pt-1 text-md font-mono tracking-wide text-sky-800">
                                       <span className="font-black font-mono">GITHUB ACCOUNT:  </span>
                                       {userData.github_username ? userData.github_username : 'None Connected'}
                                   </p>
                               </li>
                               <l>
                                   <p className="text-justify pt-1 text-md font-mono tracking-wide text-sky-800">
                                       <span className="font-black font-mono">SELECTED REPO:  </span>
                                       {userData.github_repo ? userData.github_repo : 'None Selected'}

                                   </p>
                               </l>
                           </ul>
                        </div>
                        <div className="rounded-2xl flex items-center justify-center pb-2">
                            <button className="bg-blue-600 hover:bg-slate-100 self-center text-white font-mono tracking-wide shadow-[1.5px_2px_1.0px_0.7px_rgba(0,0,0,0.48)] hover:white hover:text-blue-500 hover:border-gray-200 text-lg font-bold py-3 px-10 rounded-3xl mt-4 mb-6" type="button">
                                <svg xmlns="http://www.w3.org/2000/svg" className="h-7 w-6 inline-block ml-20" fill="currentColor" viewBox="0 0 24 24">
                                    <path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/>
                                </svg>
                                <a className="pl-5 pr-20 py-5 tracking-wide" href='/authorize/github'>GitHub</a>
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

