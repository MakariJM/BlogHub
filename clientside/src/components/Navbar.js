import React from 'react';
import { Navbar, Nav } from 'react-bootstrap';

const NavBar = () => (
  <Navbar bg="primary" variant="dark" expand="lg">
    <Navbar.Brand href="/">BlogHub</Navbar.Brand>
    <Navbar.Toggle aria-controls="responsive-navbar-nav" />
    <Navbar.Collapse id="responsive-navbar-nav">
      <Nav className="mr-auto">
        <Nav.Link href="/">Home</Nav.Link>
        <Nav.Link href="/blogs">Blogs</Nav.Link>
        <Nav.Link href="/comments">Comments</Nav.Link>
        <Nav.Link href="/about">About Us</Nav.Link>
        <Nav.Link href="/signup">Sign Up</Nav.Link>
      </Nav>
    </Navbar.Collapse>
  </Navbar>
);
export default NavBar;
