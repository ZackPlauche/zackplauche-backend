<template>
    <div class="about">
        <hero class="overlay overlay-dark">
            <h1>About Me</h1> 
            <p class="subtitle">Get to know me and my hobbies.</p>
        </hero>
    </div>
</template>

<script>
    import Hero from "@/components/Hero.vue";

    export default {
        name: "About",
        components: {
            Hero,
        },
    };
</script>