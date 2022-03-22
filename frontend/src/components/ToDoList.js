const ToDoItem = ({todo}) => {
    return (
        <tr>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.text_note}
            </td>
            <td>
                {todo.date_of_creation}
            </td>
             <td>
                {todo.update_date}
            </td>
            <td>
                {todo.user}
            </td>
            <td>
                {todo.is_active}
            </td>
        </tr>
    )
}


const ToDoList = ({todos}) => {
    return (
        <table>
            <th>
                Name of project
            </th>
            <th>
                Text of note
            </th>
            <th>
                Date of creation
            </th>
            <th>
                Update date
            </th>
             <th>
                Username
            </th>
             <th>
                Status is_active
            </th>
            {todos.map((todo) => <ToDoItem todo={todo} />)}
        </table>
    )
}


export default ToDoList