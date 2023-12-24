
const { useState, useEffect } = React;

const AccountUserInfo = (userData, reportData) => {
    return (
        <div className="lg:col-span-3 md:col-span-1 sm:col-span-1 sm:col-span-3 justify-center">
            <div className="bg-blue-500 py-10 px-10 my-2 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl">
                <div className="grid grid-flow-col gap-8 self-center bg-blue-200 py-10 px-15 my-6 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl">
                    <div className="col-span-1 ml-10 py-10 px-18 bg-blue-50 rounded-3xl shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
                        <div className="bg-blue-50 rounded-2xl pl-10">
                            <p className="text-left pl-18 text-md font-mono tracking-wide">
                                <span className="pl-8 font-semibold">ACCOUNT:  </span> {userData.name}
                            </p>
                            <p className="text-left ml-18 pt-1 text-md font-mono tracking-wide">
                                <span className="pl-8 font-bold font-mono">EMAIL:   </span> {userData.userid}
                            </p>
                            <p className="text-left ml-18 pt-1 text-md font-mono tracking-wide">
                                <span className="pl-8 font-bold font-mono">USERNAME:  </span> {userData.username}
                            </p>
                            <p className="text-left pl-18 pt-1 text-md font-mono tracking-wide">
                                <span className="pl-8 font-bold font-mono">NUMBER OF REPORTS SAVED:  </span> {reportData.length}
                            </p>
                        </div>
                    </div>
                    {/*<div className="col-span-1"></div>*/}
                    <div className="col-span-1 mr-10 py-10 bg-blue-50 rounded-3xl shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
                        <h3 className="self-center text-center text-blue-600 text-lg text-center font-semibold font-mono pb-3">Authorize
                            Github Account</h3>
                        <div className="bg-blue-50 rounded-2xl mx-0 min-w-full flex flex-col items-center">
                            <button className="bg-sky-500 hover:bg-slate-100 self-center text-white font-mono tracking-wide shadow-[1.5px_2px_1.0px_0.5px_rgba(0,0,0,0.48)] hover:white hover:text-blue-500 hover:border-gray-200 text-lg font-semibold py-3 px-20 rounded-3xl mt-2 mb-3" type="button">
                                <a className="px-10 py-2 tracking-wide" href='/authorize/github'>Authorize Account</a>
                            </button>
                        </div>
                    </div>
                    {/*<div*/}
                    {/*    className="col-span-1 mr-10 py-8 bg-blue-50 rounded-3xl shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">*/}
                    {/*    <div className="bg-blue-50 rounded-2xl pl-10">*/}

                    {/*    </div>*/}
                    {/*</div>*/}
                </div>
            </div>
        </div>
    )
}