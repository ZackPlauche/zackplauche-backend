<template>
    <div class="about-me">
        <img :src="image.url" :alt="image.alt">
        <div class="about-me-text">
            <h2>{{ heading }}</h2>
            <p v-html="body"></p>
        </div>
    </div>
</template>

<script>
export default {
    name: 'AboutMe',
    props: {
        heading: String,
        body: String,
        image: Object,
    }
}
</script>

<style scoped>
    .about-me {
        display: flex;
        flex-wrap: wrap;
        gap: 50px;
        width: 100%;
    }
    
    img {
        flex-shrink: 1;
        flex-basis: 400px;
        max-width: 400px;
        border-radius: 100vh;
    }

    .about-me-text {
        flex-grow: 1;
        flex-basis: 400px;
    }
    
    h2 {
        font-size: 52px;
        margin-bottom: 20px;
    }
    
    p {
        font-size: 20px;
        line-height: 30px;
    }
    
</style>