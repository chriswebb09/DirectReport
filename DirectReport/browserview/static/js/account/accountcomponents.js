
const { useState, useEffect } = React;

const AccountUserInfo = (userData, reportData) => {
    return (
        <div className="lg:col-span-3 md:col-span-1 sm:col-span-1 sm:col-span-3 justify-center">
            <div className="bg-blue-500 py-10 px-14 my-2 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl">
                <div
                    className="grid grid-flow-col gap-10 self-center bg-blue-200 py-10 px-15 my-6 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl">
                    <div
                        className="col-span-1 ml-10 py-10 px-15 bg-blue-50 rounded-3xl shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
                        <div className="bg-blue-50 rounded-2xl pl-20">
                            <p className="text-left pl-18 text-sm tracking-wide">
                                <span className="pl-4 font-semibold">ACCOUNT:  </span> {userData.name}
                            </p>
                            <p className="text-left ml-18 pt-1 text-sm tracking-wide">
                                <span className="pl-4 font-bold">EMAIL:   </span> {userData.userid}
                            </p>
                            <p className="text-left ml-18 pt-1 text-sm tracking-wide">
                                <span className="pl-4 font-bold">USERNAME:  </span> {userData.username}
                            </p>
                            <p className="text-left pl-18 pt-1 text-sm tracking-wide">
                                <span className="pl-4 font-bold">NUMBER OF REPORTS SAVED:  </span> {reportData.length}
                            </p>
                        </div>
                    </div>
                    <div className="col-span-1 py-8 bg-blue-50 rounded-3xl shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
                        <div className="bg-blue-50 rounded-2xl pl-10">

                        </div>
                    </div>
                    <div
                        className="col-span-1 mr-10 py-8 bg-blue-50 rounded-3xl shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
                        <div className="bg-blue-50 rounded-2xl pl-10">

                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}