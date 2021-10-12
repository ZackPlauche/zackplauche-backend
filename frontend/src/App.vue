<template>
    <header>
        <navbar />
    </header>
    <main>
        <router-view v-slot="{ Component }">
            <transition name="slide-in">
                <component :is="Component"/>
            </transition>
        </router-view>
    </main>
    <Footer :copyright="copyright" :socialLinks="socialLinks" />
</template>

<script>
    import Footer from "@/components/Footer.vue";
    import Navbar from "@/components/Navbar.vue";

    export default {
        components: {
            Footer,
            Navbar,
        },
        data() {
            return {
                copyright: {
                    company: "Zack Plauché",
                    year: "2019 - 2021",
                },
                socialLinks: [
                    {
                        url: "https://www.facebook.com/zackplauche",
                        platform: "Facebook",
                    },
                    {
                        url: "https://www.instagram.com/zackplauche",
                        platform: "Instagram",
                    },
                ],
            };
        },
    };
</script>

<style lang="scss">
    :root {
        --green: #4dde21;
        --red: red;
        --primary: #21abde;
        --primary-dark: #004a66;
        --primary-super-dark: #0c181e;
        --secondary: #00d1e6;

        --base-font: "Montserrat";
        --display-font: "Bentham";
        --heading-font: var(--display-font);
    }

    * {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
    }

    body {
        font-family: var(--base-font);
    }

    main {
        min-height: calc(100vh - var(--navbar-height));
        width: 100%;
        position: relative;
    }

    h1,
    h2,
    h3,
    h4,
    h5,
    h6 {
        color: var(--primary-dark);
    }

    .text-primary { color: var(--primary); }
    .text-primary-dark { color: var(--primary-dark); }
    .text-secondary { color: var(--secondary); }
    .text-left { text-align: left; }

    .overlay {
        position: relative;

        & > * {
            position: relative;
            z-index: 1;
        }

        &::after {
            content: "";
            background-color: black;
            opacity: 0.3;
            position: absolute;
            top: 0;
            right: 0;
            bottom: 0;
            left: 0;
        }
    }

    .container {
        width: 90%;
        max-width: 1440px;
        margin: 0 auto;
    }

    .btn {
        display: inline-block;
        cursor: pointer;
        text-decoration: none;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        text-transform: capitalize;
    }

    .background-image {
        position: absolute;
        height: 100%;
        width: 100%;
        top: 0;
        object-fit: cover;
        object-position: center;
        z-index: -1;
    }

    .fade-enter-active,
    .fade-leave-active {
        transition: opacity 0.5s ease;
    }

    .fade-enter-from,
    .fade-leave-to {
        opacity: 0;
    }

    .slide-out-enter-active,
    .slide-out-leave-active,
    .slide-in-enter-active,
    .slide-in-leave-active {
        transition: right .5s ease;
        top: 0;
        width: 100%;
        position: absolute;
    }
    
    .slide-in-enter-to,
    .slide-in-leave-from,
    .slide-out-enter-to,
    .slide-out-leave-from {right: 0;}

    .slide-out-enter-from {right: 100%;}
    .slide-out-leave-to {right: -100%;}
    .slide-in-enter-from {right: -100%;}
    .slide-in-leave-to {right: 100%;}


</style>