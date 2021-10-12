<template>
    <nav class="navbar">
        <router-link class="navbar-logo" :to="{ name: 'Home' }">{{ appName }}</router-link>
        <ul class="navbar-menu">
            <li><router-link class="nav-link" :to="{ name: 'Home' }">Home</router-link></li>
            <li><router-link class="nav-link" :to="{ name: 'About' }">About</router-link></li>
            <li><a class="nav-link" href="">Contact</a></li>
        </ul>
    </nav>
</template>

<script>
export default {
    name: 'Navbar',
}
</script>

<style lang="scss">
:root {
    --navbar-height: 60px;
}

.navbar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: var(--navbar-height);
    background-color: white;
    position: relative;
    padding: 0px 5vw;
    
    a {text-decoration: none}
}

.navbar-menu {
    display: flex;
    list-style: none;
    gap: 20px;
}

.navbar-logo {
    color: var(--primary);
    font-size: calc(var(--navbar-height) * .7);
    font-family: var(--base-font);
    font-weight: 100;
    transition: color .2s ease;
    
    &:hover {color: black}
}

li .nav-link {
    text-transform: uppercase;
    font-weight: 900;
    color: black;
    transition: color .2s ease;
    
    &:hover {color: var(--primary)}
}

li:nth-child(2) .nav-link:hover {color: var(--red)}
li:nth-child(3) .nav-link:hover {color: var(--green)}
</style>