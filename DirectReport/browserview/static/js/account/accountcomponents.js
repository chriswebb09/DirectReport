
const { useState, useEffect } = React;

const AccountUserInfo = (userData, reportData) => {
    return (
        <div className="lg:col-span-3 md:col-span-1 sm:col-span-3 justify-center">
            <div className="bg-blue-500 py-10 px-14 my-2 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl">
                <div className="grid grid-flow-col gap-10 self-center bg-blue-200 py-10 px-15 my-6 shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)] rounded-3xl">
                    <div className="col-span-1 ml-10 py-10 px-15 bg-blue-50 rounded-3xl shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
                        <div className="bg-blue-50 rounded-2xl pl-10">
                            <h1 className="text-left pl-10">
                                <span className="pl-4 font-semibold">Account:  </span> {userData.name}
                            </h1>
                            <h1 className="text-left pl-10 pt-1">
                                <span className="pl-4 font-semibold">Email:   </span> {userData.userid}
                            </h1>
                        </div>
                    </div>
                    <div className="col-span-1 mr-10 py-8 bg-blue-50 rounded-3xl shadow-[1.0px_1.0px_5.0px_0.0px_rgba(0,0,0,0.58)]">
                        <div className="bg-blue-50 rounded-2xl pl-10">
                            <p className="text-left pl-4 ml-10 pt-1">
                                <span className="pr-11 font-semibold">Username:  </span> {userData.username}
                            </p>
                            <p className="text-left pl-4 ml-10 pt-1">
                                <span className="pr-4 font-semibold">Number of reports saved:  </span> {reportData.length}
                            </p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}