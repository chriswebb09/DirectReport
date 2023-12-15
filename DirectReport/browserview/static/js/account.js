
const { useState, useEffect } = React;

const AccountUserInfo = (userData, reportData) => {
    return (
        <div className="lg:col-span-3 md:col-span-1 sm:col-span-3 justify-center">
            <div className="grid grid-flow-col gap-10 shadow-lg self-center bg-blue-200 py-6 px-5 my-2 shadow-lg rounded-3xl">
                <div className="col-span-1 py-6 bg-blue-50 rounded-3xl">
                    <div className="bg-blue-50 rounded-2xl pl-20">
                        <h1 className="text-left pl-5">
                            <span className="pr-4 font-semibold">Account:  </span>{userData.name}
                        </h1>
                        <h1 className="text-left pl-5 pt-1">
                            <span className="pr-10 font-semibold">Email:   </span> {userData.userid}
                        </h1>
                    </div>
                </div>
                <div className="col-span-1 py-6 bg-blue-50 rounded-3xl">
                    <div className="bg-blue-50 rounded-2xl pl-20">
                        <p className="text-left pl-4 pt-1">
                            <span className="pr-11 font-semibold">Username:  </span> {userData.username}
                        </p>
                        <p className="text-left pl-4 pt-1">
                            <span className="pr-4 font-semibold">Number of reports saved:  </span> {reportData.length}
                        </p>
                    </div>
                </div>
            </div>
        </div>
    )
}

const Account = () => {
    const [userData, setUserData] = useState({});
    const [actualData, setActualData] = useState({});
    const [reportData, setReportData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch(`/account_data`)
            .then((response) => {
                if (!response.ok) {
                    throw new Error(
                        `This is an HTTP error: The status is ${response.status}`
                    );
                }
                return response.json();
            })
            .then((actualData) => {
                setUserData(actualData["user"]);
                setReportData(actualData["reports"]);
                setActualData(actualData);
                setError(null);
            })
            .catch((err) => {
                setUserData(null)
                setReportData(null)
            })
            .finally(() => {
                setLoading(false);
            });
    }, []);

    if (loading) {
        return (
            <div>{`There is a problem fetching the post data - ${error}`}</div>
        )
    } else {
        return (
            <div className="mx-50 content-center mt-0 mb-48 h-150">
                <div className="pt-5 pb-3 mt-0 mb-5 ml-20 px-20">
                    <h1 className="text-2xl text-blue-800 text-left font-bold font-mono pt-5">
                        User Account
                    </h1>
                </div>

                <div className="grid grid-cols-3 gap-8 mb-1 mx-20 px-20 justify-center">
                    {userData && AccountUserInfo(userData, reportData)}
                </div>
            </div>
        )
    }
};

const domContainer = document.querySelector('#root');
ReactDOM.render(<Account/>, domContainer);