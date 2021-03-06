import React from 'react';
import logo from './logo.svg';
import './App.css';


class App extends React.Component{
  render(){
    return(
      <div className='container'>
        <div id='task-container'>
          <div id='form-wrapper'>
            <form id='form'>
              <div className='flex-wrapper'>
                <div style={{flex:6}}>
                  <input className='form-control' id='title' type='text' name='title' placeholder='Add task'></input>
                <div style={{flex:1}}>
                  <input id='submit' className='btn btn-warning' type='submit'></input>
                  
                </div>
                </div>
              </div>
            </form>

          </div>
          <div id='list-wrapper'>

          </div>
        </div>
        
        
      </div> 
    )
  }

}
export default App;
