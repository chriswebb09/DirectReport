
const { useState, useEffect } = React;

const Account = () => {
    const [userData, setUserData] = useState({});
    const [reportData, setReportData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        document.getElementById('AuthSpinnerUI').classList.toggle("hidden");
        fetch('/api/account_data')
            .then((response) => {
                if (!response.ok) {
                    throw new Error(
                        `This is an HTTP error: The status is ${response.status}`
                    );
                }
                return response.json();
            })
            .then((responseData) => {
                setUserData(responseData["user"]);
                setReportData(responseData["reports"]);
                setError(null);
            })
            .catch((err) => {
                setUserData(null);
                setReportData(null);
                setError(err.message);
            })
            .finally(() => {
                setLoading(false);
                document.getElementById('AuthSpinnerUI').classList.toggle("hidden");
            });
    }, []);

    if (loading) {
        return (
            <div className="my-50 py-20">
                <div className="py-10 mt-20">
                    <AuthSpinnerUI/>
                </div>
                <div className="mx-0 min-w-full flex flex-col items-center">
                    <div className="mt-10 py-10">{`There is a problem fetching the post data - ${error}`}</div>
                    <div className="mt-20 py-20"></div>
                </div>
            </div>
        )
    } else {
        return (
            <div className="mx-20 content-center mt-0 mb-0 h-41">
                <h1 className="self-center text-center text-2xl text-blue-800 text-center font-bold font-mono pt-5 pb-5 mx-30 px-20">User Account Data</h1>
                <div className="grid grid-cols-3 gap-8 mx-20 px-30 mt-0 justify-center">
                    {userData && AccountUserInfo(userData, reportData)}
                </div>
            </div>
        )
    }
};


const domContainer = document.querySelector('#root');
ReactDOM.render(<Account/>, domContainer);