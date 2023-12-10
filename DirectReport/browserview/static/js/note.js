'use strict';
const elem = React.createElement;


const rootElement = document.getElementById('root')
const dateItem = new Date(data.created_at).toLocaleDateString()

class Entry extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            isEditting: false,
            topic: '',
            entry: '',
            modified_on: ''
        };

        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
        this.handleChange2 = this.handleChange2.bind(this);
    }



    handleSubmit(event) {
        event.preventDefault();
        axios({
            method: 'post',
            url: "http://127.0.0.1:5000/entry/" + this.props.itemdata.uuid,
            headers: {'content-type': 'application/json'},
            data: {"id": this.props.itemdata.uuid, "entry": this.props.itemdata.message, "topic": this.props.itemdata.topic, "created_at": this.props.itemdata.created_at, "week_id": this.props.itemdata.week_uuid, day_id: this.props.itemdata.day_uuid}
        }).then(result => {
            console.log(result.data)
        }).catch(error => {
            console.log(error);
        })
        this.click();
    }

    handleChange(event) {
        this.setState({topic: event.target.value});
        this.props.itemdata.topic = event.target.value;
    }

    handleChange2(event) {
        this.setState({entry: event.target.value});
        this.props.itemdata.message = event.target.value;
    }

    renderTopicElement = () => {

        if (this.state.isEditting) {
            return <form className="w-3/4 mx-2 my-10 py-5 px-4 self-center bg-gray-100 rounded-xl shadow-md" onSubmit={this.handleSubmit}>
                <h1 className="my-10 text-3xl text-gray-600 text-center content-center font-bold">Edit</h1>
                <div className="flex my-10 mx-40">
                    <div class="w-1/6">
                        <label className="text-2xl text-gray-600 font-medium text-right mb-1 mb-0 pr-2">Topic:</label>
                    </div>
                    <div class="w-5/6">
                        <input className="content-center rounded w-full" type="text" value={this.props.itemdata.topic} onChange={this.handleChange}></input>
                    </div>
                </div>
                <div className="flex my-10 mx-40">
                    <div class="w-1/6">
                        <label className="text-2xl text-gray-600 font-medium text-right mb-1 mb-0 pr-2">Entry: </label>
                    </div>
                    <div class="w-5/6">
                        <textarea rows="10" className="focus:shadow-soft-primary-outline min-h-unset text-sm leading-5.6 ease-soft block h-auto w-full appearance-none rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 outline-none transition-all placeholder:text-gray-500 focus:border-fuchsia-300 focus:outline-none" value={this.props.itemdata.message} onChange={this.handleChange2}>{this.props.itemdata.message}</textarea>
                    </div>
                </div>
                <div className="flex justify-center my-8">
                    <button className="self-center bg-blue-500 hover:bg-gray-400 text-white text-xl font-semibold py-4 px-6 rounded-lg" type="submit">Update</button>
                </div>
            </form>
        } else {
            return <div className="w-3/4 bg-gray-100 mx-8 my-10 py-12 rounded-xl px-2 self-center shadow-md">
                <h1 className="mb-5 text-3xl text-gray-600 text-center content-center font-bold">{'Topic: ' + this.props.itemdata.topic}</h1>
                <p className="mt-8 px-40 text-xl content-center text-gray-500 border-0">{'Entry: ' + this.props.itemdata.message}</p>
                <h2 className="my-2 px-40 text-lg text-gray-500 font-semibold">{'Created on: ' +   dateItem}</h2>
                <div className="flex flex-row items-center content-center mx-20 space-x-10">
                    <div className="ml-20 bg-gray-200 rounded-xl my-6 px-2 py-2 w-1/4">
                        <h1 className="py-1 text-lg text-gray-600 font-bold">Notes</h1>
                        <ul className="list-disc list-inside px-2 py-1">
                            {this.props.itemdata.notes.map(note =>
                                <li className="text-gray-600">{note.note}</li>
                            )}
                        </ul>
                    </div>
                    <div className="mx-10 bg-gray-200 rounded-xl my-6 px-3 py-2 w-1/4">
                        <h1 className="py-1 text-lg text-gray-600 font-bold">Blockers</h1>
                        <ul className="list-disc list-inside px-2 py-1">
                            {this.props.itemdata.blockers.map(blocker =>
                                <li className="text-gray-600">{blocker.blocker}</li>
                            )}
                        </ul>
                    </div>
                    <div className="bg-gray-200 rounded-xl my-6 px-3 py-2 w-1/4">
                        <h1 className="py-1 text-lg text-gray-600 font-bold">Jira's</h1>
                        <ul className="list-disc list-inside px-2 py-1">
                            {this.props.itemdata.jiras.map(jira =>
                                <li className="text-gray-600">{"Ticket: " + jira.jira_ticket + " Tag: " + jira.jira_tag}</li>
                            )}
                        </ul>
                    </div>
                </div>
                <div className="my-10 flex content-center items-center justify-center gap-x-24">
                    <button className="my-15 rounded-xl bg-blue-500 px-16 py-5 text-lg text-white shadow-md font-semibold text-center hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500" onClick={this.click}>Edit</button>
                    <a href={"/delete/" + this.props.itemdata.uuid} className="mt-50 rounded-xl bg-blue-500 px-14 py-5 text-lg text-white shadow-md font-semibold text-center hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-500">Delete</a>
                </div>
            </div>
        }
    }

    click = () => {
        this.setState((state) => ({
            ...state,
            isEditting: !state.isEditting
        }));
    }

    render() {
        return (
            <div className="flex flex-col justify-center my-6 mx-60">
                {this.renderTopicElement()}
            </div>
        );
    }
}

function App() {
    return (
        <div>
            <Entry name="Entry" itemdata={data}/>
        </div>
    )
}

ReactDOM.render(<App/>, rootElement);