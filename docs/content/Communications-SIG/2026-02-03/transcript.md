SIG: Communications SIG
Date: 2026-02-03
Duration: 12 minutes
Zoom Recording URL: https://zoom.us/rec/share/VjFajSnxjTDok5OD_EE9S3XTeewe47vKqvl1zvffTj1daxNe_5pgM3wpamI4_yIL.zIeITkA8e6YUhyNy
============================================================

## Zoom Recording Transcript

**Kasper Nissen** 02:18 Hello?
**Jay DeLuca** 02:22 Hello, Casper. How's it going?
**Kasper Nissen** 02:24 Good, good. You?
**Jay DeLuca** 02:26 Pretty good, can't complain.
I think a lot of the normal people who join this meeting are traveling back from, The unlock the conference.
**Kasper Nissen** 02:35 Yeah, I could imagine.
I just wanted to, to join and listen in. Now I have the time. Usually, it's, so I'm based in Denmark, so usually this time is not really good, with kids and dinner and everything, but, today was… I was okay, so, just joining to listen in.
**Jay DeLuca** 02:58 Glad to have you. We'll see if we'll see if there's anything to discuss.
**Kasper Nissen** 03:02 Interesting, but .
**Jay DeLuca** 03:04 Yeah, glad you're able to make it.
Are you, interested in any particular part of OpenSelemetry?
**Kasper Nissen** 03:12 I'm writing a few blog posts, I actually have 4 blog posts right now that I'm looking to publish very, very soon, around.
**Jay DeLuca** 03:20 Awesome.
**Kasper Nissen** 03:20 egress controllers, and, I just proposed the other, what was it, Friday? Like, a maturity framework on the community repo.
**Jay DeLuca** 03:30 Yes, I saw that.
**Kasper Nissen** 03:32 Yeah, how to assess, like, CNCF projects, or basically any project on total maturity, and I've now applied that to… to my evaluation of, right now, four ingress controllers.
So I'm trying to see how it works, whether it makes sense or not, and… A few blog posts comes out of that, so hopefully we can get those on the blog as well at some point.
**Jay DeLuca** 03:55 Yeah, I… I wanna… I wanna follow that… that issue and that discussion closely, because it… it'll… I think it tangentially aligns with a project that I'm working on called the Ecosystem Explorer, where I'm also trying to surface a lot of, metadata and, like, a lot more technical details about the various components in the ecosystem.
And then, one of the end goals, once we have all that information, is to be able to, like, do analysis on, like, conformance to, like, certain semantic conventions, and, and I see that fitting into the maturity model of around, like.
even for instrumentations, like, for a given instrumentation, does it support metrics, logs, traces? Do they adhere to semantic conventions? What other available options do you have to use, though?
I think that's… that's great.
**Kasper Nissen** 04:49 Whereas… is that work happening in the ecosystem? Because then I would like to follow that as well, somehow.
**Jay DeLuca** 04:57 Yeah, so, there's this… We just started the repo for it.
**Kasper Nissen** 05:07 slower. Okay.
**Jay DeLuca** 05:08 Yeah, and I have a proof of concept That I had created, over here, and so this, this is basically specifically for the Java agent, and all the various instrumentations. So, like, if you wanted to say, like, okay, if I'm using Cassandra and using the Java agent, Like, what do I get? And so, like, we have… it tells you these are the spans, it shows you, you know, these are the spans that adhere to our semantic conventions, and there's actually a configuration flag, and when you opt into that configuration flag, you then get this metric.
And yeah, so… Oh, that's kind of… this is the proof of concept, but right now, we're in the process of, like, creating a registry, essentially, for all of the base information, and it's version-aware, because I think one of the other things that, is currently confusing with a lot of our documentation is, like.
if I'm running X version of whatever, does this version of the documentation apply to what I'm looking at? And so that's the only type of thing that I'm trying to solve there.
**Kasper Nissen** 06:18 Oh, that's nice. I definitely want to follow that as well. That sounds… that sounds, like, familiar to what I'm trying to propose as well, to some extent. Not as, like… deep technical analysis on, like, on a more lower level, but… but I think my… the proposal is… is… can be both very low and very high, to the sense that… that just looking overall at the project, where is… where is it on the… on the different dimensions, but also going deep down and looking at, okay, do… what kind of resource attributes are we providing? Are we getting… Yeah, are we sending metrics over OTLP? Are we using Prometheus? What is going on in this particular project?
But yeah, that makes a lot of sense. Cool. I'll, definitely, follow that. Nice.
**Jay DeLuca** 07:04 Yeah, ditto, ditto, and I'll follow yours as well. Yeah, I mean, it sounds like there's very similar goals around just, like.
Whether it's deeper or high level, just understanding The current state of what's available to people, so…
**Kasper Nissen** 07:18 Yeah, and try to… so much of this work comes from reaching out to projects already and just working with them, so it's also a tool to say, hey, this is sort of our evaluation right now of where you are. This is, like, the dimensions we think you should probably work a little bit on, or we can help you, like, progress into a better state for supporting OTEL in this space. So it's basically just, like a… like a tool to highlight where things are, and use it for discussions, to hopefully push the ecosystem a bit more.
on adopting, because I think, as it is right now, with the hotel adoption, as it is right now, we need to have… we need to ensure that all the projects are also following along. People are starting to expect to have really good hotel support in the products they're using, and at least from my experience working with the Ingress controllers, it's… it's a little bit… there's still work to be done in that space, let me just put it that way.
**Jay DeLuca** 08:19 Yeah, things are moving quickly, and the parity between signals or technologies is all over the place, so…
**Kasper Nissen** 08:26 Yeah.
Oh, sorry for hijacking.
**Jay DeLuca** 08:30 I mean, we don't have any other topics here, so… Hey, Sophia.
Find the mute button.
**Kasper Nissen** 08:40 Anyways…
**Jay DeLuca** 08:41 I feel like I spent half my day doing that.
I still can't hear ya.
**Kasper Nissen** 08:48 No, Mike is not.
**Jay DeLuca** 08:54 Still can't.
**Sophia Solomon** 08:55 Hello. Can you hear me now?
**Jay DeLuca** 08:56 There it is.
**Kasper Nissen** 08:57 There it is, yes.
Yeah.
**Sophia Solomon** 09:00 I was just in a meeting before this, too, and… I don't know, it just escapes me.
**Jay DeLuca** 09:08 No worries.
But yeah, so I don't know, if anyone else is, is gonna show up today.
**Sophia Solomon** 09:16 Yeah, it seems kind of empty.
**Jay DeLuca** 09:17 Yeah, I know a lot of people are traveling back from the unconference in Brussels. I know, like.
Severin, Marillia, Tiffany, They were all there, at least.
**Sophia Solomon** 09:28 No.
**Jay DeLuca** 09:29 And I know, Vitor said that he was gonna be potentially 15 minutes late.
Yeah, I mean, I don't… if we don't have any other topics, we might be able to… End a little bit early today, but…
**Sophia Solomon** 09:44 Yeah.
I mean, the only thing I wanted to bring up was that, the hotel end user seg were having a couple of hotel and practice, events coming up, February the 12th and February 18th.
And they're posted in the comms chat, so if you guys want to check that out at all.
Feel free.
And… yeah.
**Jay DeLuca** 10:09 Are those, in person, or are those virtual?
**Sophia Solomon** 10:12 They'll be virtual, yeah, so, the links are… Under the posts.
**Jay DeLuca** 10:23 Cool.
Yeah, that's about it.
Yeah, I guess, anything, anything else?
**Sophia Solomon** 10:36 No.
**Jay DeLuca** 10:38 Alright, cool.
**Kasper Nissen** 10:40 maybe just a quick question from my side. So, as I mentioned earlier, I'm doing multiple blog posts, just as a preference from the maintainer perspective. Is it better to create like, a single issue listing all the different posts, or is it better to create multiple issues and then have multiple PRs per post, or is there any, like, preferences in that space regarding multiple posts in a series?
**Jay DeLuca** 11:08 I can't tell you definitively, but I would say, from my opinion, I think a single issue you definitely want to have multiple PRs for each post, but I think a single issue, if they're all related, I think that's perfectly fine. I think just the… really the important piece is just that there's a tracking issue where if someone has comments or they want to collaborate, there's some mechanism to do that. But yeah, I don't think it necessarily needs to be multiple issues.
**Sophia Solomon** 11:37 I know, because with the docs refactoring, Tiffany has, one big issue, like, one big, PR for all the issues, and then she has links, for each one, so… I think one big one is good.
**Kasper Nissen** 11:51 Perfect. Then I will do it like that.
Awesome, thanks, and thank you.
**Jay DeLuca** 11:58 All right, well, we'll end it there then. So, everybody have a great day, and see you next time.
**Sophia Solomon** 12:03 You too. Bye. Bye.
