import React from 'react';

const Menu = () => {
    return (
        <menu style={{listStyleType: 'none', display: 'flex'}}>
            <li><a style={{marginRight: '40px'}} href="#">Все пользователи</a></li>
            <li><a style={{marginRight: '40px'}} href="#">Проекты</a></li>
            <li><a style={{marginRight: '40px'}} href="#">TODO</a></li>
        </menu>
    )
}

export default Menu;