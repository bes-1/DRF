import React from "react";

class ToDoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'text_note': '',
            'users': '',
            'projects': '',
        }
    }


    handleSubmit(event) {
        this.props.newToDo(this.state.text_note, this.state.users, this.state.projects)
        event.preventDefault()
    }

    handleUsersChange(event) {
        if (!event.target.selectedOptions) {
            return
        }

        let users = []
        for (let i = 0; i < event.target.selectedOptions.length; i++) {
            users.push(parseInt(event.target.selectedOptions.item(i).value))
        }

        this.setState({
            'users': users[0]
        })
    }

    handleProjectsChange(event) {
        if (!event.target.selectedOptions) {
            return
        }
        let projects = []
        for (let i = 0; i < event.target.selectedOptions.length; i++) {
            projects.push(parseInt(event.target.selectedOptions.item(i).value))
        }

        this.setState({
            'projects': projects[0]
        })
    }

    handleTextNoteChange(event){
        this.setState({
            [event.target.name]: event.target.value
        })
    }

    render() {
        return (
            <form onSubmit={(event => this.handleSubmit(event))}>
                <input
                    type="text"
                    name="text_note"
                    placeholder="text_note"
                    onChange={(event => this.handleTextNoteChange(event))}
                    value={this.state.text_note}
                />
                {/*внутри select атрибут multiple, чтобы выбрать несколько (связь один ко многим)*/}
                <select onChange={(event => this.handleUsersChange(event))}>
                    {this.props.users.map((user) => <option
                        value={user.id}>{user.first_name} {user.last_name}</option>)}
                </select>
                <select onChange={(event => this.handleProjectsChange(event))}>
                    {this.props.projects.map((project) => <option value={project.id}>{project.name}</option>)}
                </select>
                <input
                    type="submit"
                    value='Create'
                />
            </form>
        )
    }

}

export default ToDoForm