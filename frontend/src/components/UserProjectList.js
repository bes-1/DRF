import {useParams} from "react-router-dom";

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.link_to_repository}
            </td>
            <td>
                {project.user_set}
            </td>
        </tr>
    )
}


const UserProjectList = ({projects}) => {
    var {id} = useParams()
    var filteredProjects = projects.filter((project) => project.users.includes(parseInt(id)))

    return (
        <table>
            <th>
                Name of project
            </th>
            <th>
                Link to repository
            </th>
            <th>
                Users name
            </th>
            {filteredProjects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}


export default UserProjectList