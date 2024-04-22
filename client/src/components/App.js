import Blogs from './Blogs';
import NavBar from './Navbar';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Comments from './Comments';
import SignUp from './SignUp';
import AboutUs from './AboutUS';
import Home from './Home';

function App() {
  return (
    <Router>
      <NavBar />
      <Route exact path="/" component={Home} />
      <Route path="/blogs" component={Blogs} />
      <Route path="/comments" component={Comments} />
      <Route path='/signup' component={SignUp}/>
      <Route path='/about' component={AboutUs} />
    </Router>
  );
}

export default App;