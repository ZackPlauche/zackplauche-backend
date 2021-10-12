<template>
    <div class="home">
    <Hero style="text-align: left;" :image="buildImageUrl('zack-batumi.jpg')">
        <h1>Zack Plauché</h1>
        <p class="subtitle">Let's do epic world changing sh*t together.</p>
        <router-link class="btn btn-hero" :to="{ name: 'About' }">Learn more</router-link>
    </Hero>
        <section id="projects">
            <div class="container">
                <h2 v-if="projects">My Projects</h2>
                <ProjectList :projects="projects" />
            </div>
        </section>
        <div class="container">
            <!-- <AboutMe
                :image="imageOfMe"
                heading="Hi, I'm Zack. 👋"
                body="I have a strong love for nature, humanity, my darling wife, family, friends, and creating things that make the world a better place (ESPECIALLY with other people).<br>
                     I'm extremely happy that you're here, and I'd love to learn more about you &amp; invite you to learn more about me and join me on my journey to making the world a better place.<br><br>
                     Below you'll find out about more about me, my character, my projects, beliefs, and more!"
            /> -->
        </div>
        <h2>Blog</h2>
        <BlogCarousel />
        <h2>Music</h2>
        <MusicCarousel />
        <h2>Get in Touch</h2>
        <ContactForm />
    </div>
</template>

<script>
    import Hero from "@/components/Hero.vue";
    // import AboutMe from "@/components/AboutMe.vue";
    import ProjectList from "@/components/ProjectList.vue";

    export default {
        components: {
            Hero,
            // AboutMe,
            ProjectList,
        },
        data() {
            return {
                homeHeroContent: {
                    cta: "Contact me",
                    image: this.buildImageUrl("zack-batumi.jpg"),
                    style: "text-align: left",
                },
                imageOfMe: {
                    url: this.buildImageUrl("zack-sozopal.jpg"),
                    alt: "Zack smiling standing in front of the black sea.",
                },
                projects: [
                    {
                        id: 1,
                        title: "Project #1",
                        thumbnail: this.buildImageUrl("rsz_forest.jpg"),
                    },
                    {
                        id: 2,
                        title: "Project #2",
                        thumbnail: this.buildImageUrl("rsz_forest.jpg"),
                    },
                    {
                        id: 3,
                        title: "Project #3",
                        thumbnail: this.buildImageUrl("rsz_forest.jpg"),
                    },
                    {
                        id: 4,
                        title: "Project #4",
                        thumbnail: this.buildImageUrl("rsz_forest.jpg"),
                    },
                ],
            };
        },
    };
</script>

<style scoped>
    .home-body {
        padding: 50px 0;
    }

    h2 {
        text-align: center;
        margin-bottom: 40px;
        font-size: 60px;
        font-weight: 400;
        color: var(--primary-dark);
        font-family: var(--display-font);
    }

    .about-section {
        display: grid;
        grid-template-areas:
            "heading heading heading"
            "image body body";
        gap: 10px;
    }

    .about-image {
        --size: 100%;
        height: var(--size);
        width: var(--size);
        border-radius: 100vh;
        grid-area: "image";
    }

    .about-body {
        grid-area: "body";
    }

    section {
        padding: 50px 0;
    }
</style>