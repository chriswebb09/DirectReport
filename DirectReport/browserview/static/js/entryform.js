const { useState, useEffect } = React;

class EntryForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            topic: '',
            entry: ''
        };
        this.handleTopicChange = this.handleTopicChange.bind(this);
        this.handleEntryChange = this.handleEntryChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleTopicChange(event) {
        this.setState({topic: event.target.value});
    }

    handleEntryChange(event) {
        this.setState({entry: event.target.value});
    }

    handleSubmit(event) {
        alert('A name was submitted: ' + this.state.topic + ' entry: ' + this.state.entry);
        event.preventDefault();
        axios({
            method: 'post',
            url: "http://127.0.0.1:5000/list",
            headers: {'content-type': 'application/json'},
            data: {"topic": this.state.topic, "entry": this.state.entry}
        }).then(result => {
            console.log(result.data);
        }).catch(error => {
            console.log(error);
        })
    }

    render() {
        return (
            <form className="w-3/4 py-2 px-2 self-center" onSubmit={this.handleSubmit}>
                <div class="items-center mb-6">
                    <div className="flex my-10 mr-40">
                        <div class="w-1/6">
                            <label className="text-2xl text-gray-700 font-medium text-right mb-1 mb-0 pr-2">Topic:</label>
                        </div>
                        <div class="w-5/6">
                            <input className="rounded w-full" type="text" value={this.state.topic}  onChange={this.handleTopicChange}/>
                        </div>
                    </div>
                    <div className="flex my-6 mr-40">
                        <div class="w-1/6">
                            <label className="text-2xl text-gray-700 font-medium text-right mb-1 mb-0 pr-2">Entry:</label>
                        </div>
                        <div class="w-5/6">
                            <textarea cols="70" rows="10"  className="text-base text-gray-700 placeholder-gray-600 border rounded-lg focus:shadow-outline" value={this.state.entry} onChange={this.handleEntryChange}></textarea>
                        </div>
                    </div>
                    <div className="flex justify-center my-6">
                        <button className="self-center bg-blue-500 hover:bg-gray-400 text-white text-xl font-semibold py-4 px-6 rounded-lg" type="submit">Create Account</button>
                    </div>
                </div>
            </form>
        );
    }
}