<template>
    <div class="hero" :class="{ 'hero-full': full }" :style="{ backgroundImage: `url('${image}')`}">
        <div class="container">
            <div class="hero-content">
                <slot>
                    <h1>I'm a Hero Section!</h1>
                    <p class="subtitle">I'm a subtitle (class="subtitle")</p>
                    <button class="btn btn-hero">Click me</button>
                </slot>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Hero',
        props: {
            image: {
                type: String,
                default: 'https://source.unsplash.com/1600x900/?nature',
            },
            full: {
                type: Boolean,
                default: false,
            }
        },
    }

</script>

<style lang="scss">
    .hero {
        display: flex;
        padding: 50px 0;
        justify-content: center;
        align-items: center;
        background-size: cover;
        background-position: center;
        min-height: calc(100vh - var(--navbar-height));
        text-align: center;
    }
    
    .hero.hero-full {
        height: 100vh;
        margin-top: calc(var(--navbar-height) * -1);
    }

    h1 {
        font-size: 70px;
        font-family: var(--display);
        margin-bottom: 10px;
        color: white;
    }

    .subtitle {
        font-size: 24px;
        font-weight: 400;
        color: white;
        margin-bottom: 25px;
    }

    .btn-hero {
        color: white;
        background-color: var(--primary);
        font-size: 24px;
        transition: background-color 0.2s ease, box-shadow 0.2s ease,
            color 0.2s ease;
        padding: 15px 30px;
        border-radius: 0px;

        &:hover {
            background-color: var(--primary-dark);
        }
    }

</style>