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


const ProjectList = ({projects}) => {
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
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}


export default ProjectList