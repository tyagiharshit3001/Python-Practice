import React, { useState } from 'react';
import './styles.css';

const App=()=>{

  const [users, setUsers] = useState([]);
  const loadUsers = async() =>{
    console.log('before');
    const response = await fetch ("https://reqres.in/api/users?page=1");
    const jsonresponse = await response.json();
    setUsers(jsonresponse);
  }

  return(
    <div className="App">
      <h1>Hello World</h1>
      <button onClick={loadUsers}>Get Data</button>
      <h2>Users:-</h2>
      <ul>
        {users.map((id, login)=>(<li key = {id}>Name : [login]</li>)) }
        
      </ul>
    </div>
  )
}

export default App;