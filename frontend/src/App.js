import React, {useCallback} from 'react'
import logo from './logo.svg';
import './App.css';
import UserList from './components/UserList.js'
import axios from 'axios'
import ProjectList from "./components/ProjectList.js";
import {HashRouter, BrowserRouter, Route, Routes, Link, useLocation} from "react-router-dom";
import ToDoList from "./components/ToDoList";
import UserProjectList from "./components/UserProjectList.js";
import LoginForm from "./components/LoginForm.js";
import ToDoForm from "./components/ToDoForm.js";


const NotFound = () => {
    let location = useLocation()
    return (
        <div> Page {location.pathname} not found </div>
    )
}

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'projects': [],
            'todos': [],
            'token': '',
        }
    }

    getData() {
        let headers = this.getHeader()

        axios
            .get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                const users = response.data

                this.setState({
                    'users': users
                })
            })
            .catch(error => {
                console.log(error)
                this.setState({
                    'users': []
                })
            })
        axios
            .get('http://127.0.0.1:8000/api/project/', {headers})
            .then(response => {
                const projects = response.data

                this.setState({
                    'projects': projects
                })
            })
            .catch(error => {
                console.log(error)
                this.setState({
                    'projects': []
                })
            })
        axios
            .get('http://127.0.0.1:8000/api/todo/', {headers})
            .then(response => {
                const todos = response.data

                this.setState({
                    'todos': todos
                })
            })
            .catch(error => {
                console.log(error)
                this.setState({
                    'todos': []
                })
            })
    }

    componentDidMount() {
        let token = localStorage.getItem('token')
        this.setState({
            'token': token
        }, this.getData)
    }

    isAuth() {
        return !!this.state.token
    }

    getHeader() {
        if (this.isAuth()) {
            return {
                'Authorization': 'Token ' + this.state.token
            }

        }
        return {}
    }

    getToken(login, password) {
        console.log(login, password)
        axios
            .post('http://127.0.0.1:8000/api-auth-token/', {'username': login, 'password': password})
            .then(response => {
                const token = response.data.token
                console.log(token)
                localStorage.setItem('token', token)
                this.setState({
                    'token': token
                }, this.getData)
            })
            .catch(error => console.log(error))
    }

    newToDo(text_note, users, projects) {
        let headers = this.getHeader()
        console.log(text_note, users, projects)
    }


    deleteToDo(id) {
        let headers = this.getHeader()
        console.log(id)
        axios
            .delete(`http://127.0.0.1:8000/api/todo/${id}`, {headers})
            .then(response => {
                this.setState({
                    'todos': this.state.todos.filter((todo) => todo.id != id)
                })
            })
            .catch(error => {
                console.log(error)
            })
    }

    logout() {
        localStorage.setItem('token', '')
        this.setState({
            'token': ''
        }, this.getData)
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <nav>
                        <li><Link to='/'>Users</Link></li>
                        <li><Link to='/projects'>Projects</Link></li>
                        <li><Link to='/todos'>Notes</Link></li>
                        <li><Link to='/todos/create'>New note</Link></li>
                        <li>
                            {this.isAuth() ? <button onClick={() => this.logout()}>Logout</button> :
                                <Link to='/login'>Login</Link>}
                        </li>
                    </nav>
                    <Routes>
                        <Route exact path='/' element={<UserList users={this.state.users}/>}/>
                        <Route exact path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                        <Route exact path='/todos'
                               element={<ToDoList todos={this.state.todos} deleteToDo={(id) => this.deleteToDo(id)}/>}/>
                        <Route exact path='/todos/create'
                               element={<ToDoForm users={this.state.users} projects={this.state.projects} newToDo={(text_note, users, projects) => this.newToDo(text_note, users, projects)}/>}/>
                        <Route exact path='/login'
                               element={<LoginForm getToken={(login, password) => this.getToken(login, password)}/>}/>
                        <Route path='/user/:id' element={<UserProjectList projects={this.state.projects}/>}/>
                        <Route path='*' element={<NotFound/>}/>
                    </Routes>
                </BrowserRouter>
            </div>
        )
    }
}

export default App;
