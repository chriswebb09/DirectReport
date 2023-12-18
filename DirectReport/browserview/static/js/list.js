const { useState, useEffect } = React;

const ListApp = () => {

    const [listData, setListData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch(`/getlist`)
            .then((response) => {
                if (!response.ok) {
                    throw new Error(
                        `This is an HTTP error: The status is ${response.status}`
                    );
                }
                return response.json();
            })
            .then((actualData) => {
                setListData(actualData);
                setError(null);
            })
            .catch((err) => {
                setError(err.message);
                setListData(null)
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
        if (listData.length > 0) {
            return (
                <div>
                    <EntryList name="Entry List" listdata={listData}/>
                </div>
            )
        } else {
            return (
                <div>
                    <EmptyEntryList/>
                </div>
            )
        }
    }
}

const domContainer = document.querySelector("#root");
ReactDOM.render(<ListApp/>, domContainer);
