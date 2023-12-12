
const { useState, useEffect } = React;
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
                console.log(actualData)
                setUserData(actualData["user"]);
                setReportData(actualData["reports"]);
                setActualData(actualData);
                setError(null);
                // showGraphics(actualData);
            })
            .catch((err) => {
                // setError(err.message);
                // showGraphics(null);
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
            <div className="grid grid-cols-3 gap-8 mb-1 mx-20 justify-cente">
                <div className="lg:col-span-1 md: col-span-1 sm:col-span-3 justify-center my-1">
                    <div className="shadow-lg self-center bg-blue-200 py-10 px-8 my-2 shadow-lg rounded-2xl">
                        <div className="py-10 mb-10 bg-blue-50 rounded-2xl">
                            <h1 className="text-left px-10"><span className="font-semibold">Account:</span> {userData.name}</h1>
                            <h1 className="text-left px-10"><span className="font-semibold">Email:</span> {userData.userid}</h1>
                            <p className="text-left px-10"><span className="font-semibold">Username:</span> {userData.username}</p>
                            <p className="text-left px-10"><span className="font-semibold">Number of reports saved</span> {reportData.length}</p>
                        </div>
                    </div>
                </div>
                <div className="lg:col-span-1 sm:col-span-3 justify-center my-1">
                    <div className="shadow-lg self-center bg-blue-200 py-10 px-10 my-2 shadow-lg rounded-2xl">
                        <div className="py-10 mb-20 bg-blue-50 rounded-2xl">
                            <a className="py-10 text-md hover:text-gray-200" href="/teamreport">
                                <button type="button" className="w-full text-white bg-indigo-700 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
                                    New Report
                                </button>
                            </a>
                        </div>
                    </div>
                </div>
                <div className="lg:col-span-1 sm:col-span-3 justify-center my-1">
                    <div className="shadow-lg self-center bg-blue-200 py-10 px-10 my-2 shadow-lg rounded-2xl">
                        <a className="py-10 text-md hover:text-gray-200" href="/list">
                            <button type="button" className="w-full text-white bg-indigo-700 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
                                List
                            </button>
                        </a>
                    </div>
                </div>
                <div className="col-span-3 justify-center my-1">
                    <div className="shadow-lg self-center bg-blue-200 py-10 px-8 my-2 shadow-lg rounded-2xl">
                        <div className="mx-80">
                            <a className="px-6 text-md hover:text-gray-200" href="/logout">
                                <button type="button" className="w-full text-white bg-indigo-700 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">
                                    Log Out
                                </button>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
};

const domContainer = document.querySelector('#root');
ReactDOM.render(<Account/>, domContainer);