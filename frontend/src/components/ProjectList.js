const ProjectItem = ({project, deleteProject}) => {
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
            <td>
                <button onClick={()=>deleteProject(project.id)}>Delete</button>
            </td>
        </tr>
    )
}


const ProjectList = ({projects, deleteProject}) => {
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
            {projects.map((project) => <ProjectItem project={project} deleteProject={deleteProject}/>)}
        </table>
    )
}


export default ProjectList