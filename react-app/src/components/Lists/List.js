//import { useSelector } from "react-redux";


function List(){
    //const sessionUser = useSelector(state => state.session.user);

    const testLists = [{"id": 1, "name": "First List", "user_id": 1},{"id": 2, "name": "Second List", "user_id": 1}]

    return(
        <div className="allLists">
            {testLists.map(list => (
                <li key={list.id}>{list.name}</li>
            ))}



        </div>
    )
}

export default List;
