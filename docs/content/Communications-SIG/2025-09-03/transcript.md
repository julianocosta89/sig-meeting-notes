SIG: Communications SIG
Date: 2025-09-03
Duration: 62 minutes
============================================================

## Zoom Recording Transcript

Patrice 00:00:43 Hello, hello, welcome!
Jay DeLuca 00:00:47 Lou?
TH Tiffany Hrabusa 00:00:47 Nice.
Hi, Jay.
Jay DeLuca 00:00:51 Hey. How's everybody doing?
Patrice 00:00:54 Good, how are you?
Jay DeLuca 00:00:56 Good.
Patrice 00:00:57 Nice to meet you.
Jay DeLuca 00:00:58 Yeah, you too. We've interacted on a lot of PRs, but nice to meet you face-to-face.
Is it usually a pretty light crew to these?
Meetings.
Patrice 00:01:12 It is.
Light, and lightness varies.
We've had busier.
Jay DeLuca 00:01:23 Yeah.
So it's the end of summer.
TH Tiffany Hrabusa 00:01:27 going to come. Yeah, yeah.
Patrice 00:01:29 I did think Severin was going to come, so…
Did, Agrazio mention if he would be coming? Do you know? Tiffany?
The audio cut out, but from your gestures, I figured, no.
TH Tiffany Hrabusa 00:02:07 Oh, really?
Patrice 00:02:08 Yeah.
TH Tiffany Hrabusa 00:02:08 Sorry. No, I have not heard anything from Fabrizia, so sorry about that.
Patrice 00:02:14 No, no, it's fine.
could be… Any number of reasons.
Internet.
Buds.
TH Tiffany Hrabusa 00:02:23 This is my fourth hour of meeting, so it's entirely possible that my AirPods are dying.
Patrice 00:02:28 Yes. So they're conserving as much energy as they can.
Have you pinged?
Severin?
TH Tiffany Hrabusa 00:02:50 No, but I'll do that now.
Patrice 00:02:51 Okay.
Jay DeLuca 00:02:53 Yes.
Severin Neumann 00:02:55 Hey, sorry for being late.
Patrice 00:02:57 Bye.
TH Tiffany Hrabusa 00:02:58 Hello?
Patrice 00:02:59 Hello, hello.
Severin Neumann 00:03:00 Meetings, meetings, meetings. You would mean that, like, in the evening you're done with your meetings, but yeah.
Patrice 00:03:05 It's funny.
Severin Neumann 00:03:06 to get from… International teams, right?
Hey, Jay, great to see you.
Jay DeLuca 00:03:13 Thanks, Everen. Yeah, you too.
I'm just saying that Patrice is… I interact with you guys a lot on, PRs, but it's nice to…
Get some faked face-to-face.
Severin Neumann 00:03:23 Hey, Vitor.
TH Tiffany Hrabusa 00:03:25 be here at the restaurant.
Vitor Vasconcellos 00:03:28 Hi, nice to meet you all.
How's… how's it going?
Patrice 00:03:33 Good, how are you?
Vitor Vasconcellos 00:03:35 Good, good.
Patrice 00:03:37 Another…
Vitor Vasconcellos 00:03:38 made it. No, no, no other meeting.
Patrice 00:03:41 Nice to meet you, virtually.
Vitor Vasconcellos 00:03:47 Me too.
Severin Neumann 00:03:47 Doing a face… having a face to the…
How do you say, like, to the GitHub handle.
TH Tiffany Hrabusa 00:03:56 Very helpful GitHub handle.
Patrice 00:03:59 Very.
Severin Neumann 00:04:01 Awesome. Do you want… I can share my screen if you… if you like, then I can, then we can work from our document.
Oh, let me see, I wish I did the right thing now. Can you see that?
TH Tiffany Hrabusa 00:04:16 Yes.
Severin Neumann 00:04:17 Yeah, awesome.
Just asking, Jay, since you're not a regular attendee, do you have any, like, timelines? Are you fine with, like, doing another topic first, or should we just put yours first, so you can drop off early?
Jay DeLuca 00:04:31 Nope, I'm flexible, so…
Severin Neumann 00:04:32 Okay, cool.
Then let's do it in…
that order that we have it here. If anybody wants to add any more
topics while we talk, we can definitely do that, but then let's get started. Patrice, you have added one topic here.
So, let's get started with that one.
Patrice 00:04:53 Okay, maybe it's just a, putting a toe in the water and feeling the temperature, whether we are wanting to spend any…
time addressing this at the moment. It may not be a priority.
I'd also like to bring in that,
the Linux Foundation legal team is still… assessing the various AI services, for CNCF projects.
and Linux Foundation projects, in terms of what they are…
willing to endorse, willing for us to support. So,
let me say semi-officially, even for Kappa AI, apparently legal isn't fully satisfied, but I think from the rollout… from the beginning, when we rolled this out, we were… we did make clear that it was experimental.
Severin Neumann 00:05:52 Yeah.
Patrice 00:05:52 Yeah, other CNCF projects, there is push for crowd-in, and I don't know if you've read through the
Legal terms for, open source projects, but some of the… some of the clauses are…
peculiar, and so the Linux Foundation legal team is still going through that.
Severin Neumann 00:06:15 Okay.
Patrice 00:06:16 I haven't caught up,
I guess this is kind of digressing into the… our multilingual crowd-in thing. I haven't caught up with other
PRs yet, and I probably won't be… I won't… probably won't have, caught up to speed up until mid-month this month.
So, in terms of the UK translations, in any case, I guess the question I have is.
I suppose we're holding our position, which is, it doesn't matter whether you have Crowd AI behind the scenes, or as a support tool, the
PR pipeline for any locale will be the same. We need the maintainers, we need the reviews, and we're not going to bring in
hundreds of pages at the same time. Well, I guess, unless they've been carefully reviewed, but…
Severin Neumann 00:07:11 Yeah, I mean, it's, like, the Ukrainian localization thing.
I mean, if the… if they would be up to speed, right, if we would have 3, 4, 5, like… like we have it in Portuguese, right?
This is more around, like, and this is what I tried to communicate a few times, this is right now, for me, more around building out that community, and having the people at place, and doing their stuff.
Versus, like, having the best localization in the world, right?
Because we see with, like, Portuguese and all the other languages that how important that is, first of all, to get people in, right?
And if we just have one AI-driven localization, then if this is what we want, I mean, then we can just throw out all the languages at once and have it driven by an LLM.
There's a lot of…
problems I have with that. But anyways, I mean, at some point, if, like, they have, like, a healthy community around it, and this is why I always push for, like.
we need people that feel like, hey, I'm… I'm not, like.
an approver or a maintainer for that specific localization, I am, like.
Putting on the hat for being, like, the person that…
maintains and drives how we do localizations at OpenTelemetry, we can do a lot of things, right? And I'm more than happy to hand this off at some point. I'm not, like, a good expert on that topic, and, like, we have enough things on our plate. That's on the crowdal thing, and I think we talked about this,
Many times. On the agentsMD thing, and what you said, like, I just opened it up, like, I mean, we have a policy on, like… I know it's still not in the policy, so I wanted to move it there. We have,
Gen AI policy as OpenTelemetry itself, ourselves, right? And what it says, more or less, like, hey, there's the Linux Foundation policy, and there's, like, this thing about, like.
use it with care, right, and be responsible with it. Saying that, there's a few other things that have already rolled out GitHub Copilot as, like, a GitHub
thing.
Patrice 00:09:31 And I think there's at least one other SIG that is right now requesting to have rolled out.
Severin Neumann 00:09:38 the equivalent from, I think, from a traffic.
Patrice 00:09:41 From Claude. Claude, it was… Fabrizio was…
Yeah, he was asking that, but I think this is what, like, another SIG is actively asking, I think it's the operator SIC, or something like that.
Severin Neumann 00:09:55 So if we want to have any of that for our repository, we would not, like, be the first ones, right? We could have…
But this is something where I personally want, like, all the maintainers approved, I don't think, like.
We, like, like, we should all say, like, yeah, let's enable that, and then we can see how it works. And then, yes, adding an agent's MD file totally makes sense, right?
I'm personally not against that, right? I mean.
on the back of things, everybody's now using LLMs, let's be honest, right? I mean, I also tell it, like, hey, here's the gist of what I want to write, just make it
sound English.
Patrice 00:10:37 So…
Severin Neumann 00:10:38 So, yeah, I mean, if we… if we are okay with, like, giving one of those a try.
Then let's do that, right?
I… I have no… I have no concerns here, but I'm also not the one who will say, like, yeah, let's do this and push, push, push on that, so… so that's not…
Patrice 00:10:57 Okay.
Severin Neumann 00:10:58 That's not… that important for me. Yeah, Tiffany?
TH Tiffany Hrabusa 00:11:03 I agree with everything you said, Deborah, and I would just add that
I think it's… from my perspective, we should absolutely experiment with the different options that, the Linux Foundation will let us experiment with, with the understanding that they are experiments, and that however we set them up, we should be able to roll them back.
If things go awry.
Severin Neumann 00:11:30 I think in the case of the co-pilot, it's just like, I think one GitHub admin just needs to do a checkbox to turn it on, and remove the checkbox to remove it once again. So if this is something we want to try out.
I can raise an issue on the community repo, and we have it by tomorrow, so… Yeah.
And if we want to disable it once again, it's the same flow.
Patrice 00:11:56 I, I think…
two points I would like to bring up. One regarding this particular file, it was as…
To reflect upon as hotel teams bring on various Agents.
from different companies, we're bringing in different files. We want to try and unif… you know.
agree on having agents.md, for whatever service is out there. Maybe it's premature.
I agree with Tiffany that
And I think the Linux Foundation is open to us experimenting
With whatever tools, most tools that are out there already.
I guess I wanted to avoid having claud.md, and agent.md, and copilot.md, and, so if we could kind of
if we're at that point to bring uniformity, or choose one file, that would be helpful. Even if it's only to have, okay, let's settle on agents.md, which seems generic, and then you have Claude… you point Claude to that file.
The other broader discussion, which is not for today, but
you may have thought of already, and I think
We may want to address sometime this year, is how is this… agent-enabled
How are agent-enabled capacities, now that they're out there and so many of us are using them, how will that affect
The way in which we write.
our documentation.
Fabrizio kind of brought that up in his blog post.
we…
might have a great opportunity to innovate and lead in that sense, whereas rather than just think of Hotel.io as a static
repository of information to try and, as Fabrizio said.
See it distinctly as a source for humans and a source for… Agents.
And how can we cater to both of these?
well, I guess this now new… Use case or user profile.
Severin Neumann 00:14:19 Yup.
Patrice 00:14:22 So.
Just sowing a seed, it's something that's been on my mind for the past couple of months.
I don't think AI is going away, it will just grow, and… and…
Severin Neumann 00:14:36 Yeah, probably not.
Patrice 00:14:38 what's nice about this community is I know that we… I believe we understand the limitations of the tools more than maybe some of the general public that seems to buy into certain marketing hype, but there's… there is definitely…
There are benefits to be gained in using the tools, but also in understanding the limits, one of which is
as you said, Severin, I would not endorse
Forgetting about our localization teams and just using LLM,
we're not there yet. We might never be there.
Severin Neumann 00:15:17 Yeah. No, and at the end, we're an open source community, right? I mean, it's about the people, right? I mean, in the end, like, I mean…
Patrice 00:15:27 I was in a meeting recently, and that was…
Severin Neumann 00:15:29 you are the proof that, like, our localizations are valuable, because you stepped up and said, like, hey, I help you with, like, the largest thing, right? And we need people to join our community, and the more we, like.
take away opportunities for people to contribute to our project, and even if it's them using an LLM at the back of the things and just figure out things, I'm fine with that, right? And sure, at some point, probably, yeah, we will probably have AI-generated
Localizations and whatever, but… but… I hope we have this when we have, like, a dedicated, healthy.
localization sick, right? It's maybe even independent of docs, right? I mean, that's, like, my vision of it. But yeah, we will… we will not solve this today, so…
Back to the agents in the… let's do that, right? I mean, let's… if it's, like, the generic thing, if, like, most of the LLMs support it,
if Claude, if OpenAI, if whatever is supporting that, then… then we… we should… we should add it.
or allow people to add it. I mean, if Fabristio is the one who says, like, yeah, I'm going to write that, let's have it.
Patrice 00:16:41 Okay.
Severin Neumann 00:16:43 The short version of that.
Patrice 00:16:46 Great, so then maybe I'll get back to Fabrizio. I don't remember where he commented about that, but I can communicate that with him. I just want to echo one last thing that I started mentioning before. I was in a meeting earlier this week, and what came out as the most valuable, or the top
Priority is building community around our projects. That is what will sustain the project. It's the community. It's not the LLM, it's not the AI.
Severin Neumann 00:17:18 Yeah.
Patrice 00:17:19 community.
That's it. Thanks.
Severin Neumann 00:17:24 Post.
Jade.
Jay DeLuca 00:17:27 Yeah, do you mind if I share my screen?
Severin Neumann 00:17:30 Yeah, please go ahead, let me stop sharing mine, and then…
Jay DeLuca 00:17:36 Alright.
So, I wanted to talk about… instrumentation documentation.
And I wanted to… to start the conversation, because I think it's a…
a complicated, area, but I've been exploring some things that I wanted to kind of run by you all and see where it might fit into the normal site, so…
Just a little bit of background,
you know, as a… I used to be an SRE, and now I'm a… you know, I work at Grafana, and one of the things that comes up a lot around instrumentation is, you know, how to understand what you get, what to expect, whether it's working correctly, whether it adheres to semantic conventions.
And at least in Java, it's a little bit tricky. We have some… we have some docs, and some of it's… it's pretty good. We have this supported libraries list that will give you a list of, you know, the different libraries. It gives you some notion of what
versions of the libraries we support, whether we have a standalone library instrumentation, and then, you know, some semantic conventions. But I don't think that this is all that useful, necessarily. Like, it doesn't tell me which database pool metrics, or which…
HTTP client metrics, things like that. So that's… that's one.
problem. The second is, oh, we have… and we have, like, for the individual standalone library documentation, we do have pretty decent docs for some of them. It's not always consistent, but
It does exist, but the problem is, or one of the problems is, they're not indexed by Google, so for, like, any customer or somebody who's trying to find this information, it's not all that discoverable.
It's also very technical, and there's a lot of nuance to it. So, for example, like, these are some of the questions that I was thinking, like.
If we would be able to solve
within the instrumentation documentation. So, like.
which versions of the libraries are supported automatically? What telemetry do you get from the libraries? Are there configurations that you can do to change the attributes or spans, or get more or less metrics?
I'm gonna change my auto instrumentation version, what is gonna be different? So, like, these are some of the things that, I think are important problems to solve for end users, whether it's
the person instrumenting an application, building an application, or a support person from a vendor, trying to help customers. And so, the way that I was thinking about it was, in Java, I started
aggregating some metadata. So, I have this…
And the philosophy around the way that I have aggregated this is probably a topic for a completely different discussion, but what I've done is I've built a system that automatically detects a bunch of information about our instrumentations based on some static code analysis, as well as I intercept
test, telemetry and put them into a format and analyze that. And what we get is, for all of our instrumentations, we have
you know, the instrumentation name. I'm working on adding just a very basic description. We have some other metadata around, you know, minimum Java version. We have the scope information.
The important bit, or the more important bits, I think, are the target versions, so, like, knowing which versions of your library will actually be instrumented. And then the fun stuff is the actual telemetry that's emitted. And I've been…
the way that I built it in the Java system is I can annotate the different test runs with different configurations, and we can say, okay, by default, let me find one, if you look at, like, Cassandra, we could say, by default, these are the telemetry that you get.
And then I also have this, you know, when. So, like, if you set this configuration flag, then this is the telemetry that you get. And so, that's kind of the premise of the basic metadata.
And then what I've done is I've built this UI that is built on top of it, where you can go into one of these.
So if we go to that, Cassandra, so we have this laid out of, like, this is the version 219, so the latest version of the Java agent. We have our description, the name, we have whatever configuration values are available.
We… we document the target versions, and then this is the fun stuff around, you know, by default, we can see that these are all of the…
So this instrumentation generates client spans, and this is, like, the superset of all the attributes that are emitted. And we can see, also, the semantic conventions, so by default, we emit a lot of attributes that are not SEMconv, but you can see that if you enable this feature flag of…
opt into stable semconconf, these are the attributes that you get, and they are all compliant, and so…
We can see, like, you know, these changed from…
these, you know, db.cassandra to just Cassandra. And then, you know, one of the things that's coming up is
as I mentioned, these are behind the feature flag, but in
this… 3.0 is not out yet in the Java agent, but in 3.0, we plan on making all of those things stable.
And so, an important thing to be able to know is, you know, what's gonna change. And so I put together this test, essentially, of like, this is projected what the 3.0 release will be, and you can see that, you know, these were removed.
These are… the bold ones are added, and we can see now that in that release, they will all be SEMCOM compliant.
And then one other thing that I was thinking about, you know, with the ability to do this and map all the different instrumentations.
Someone on my team in a hackathon built a CLI tool that will analyze your Gradle or Maven files for all of your dependencies, and then identify where those match to these different instrumentation libraries.
And then what you can do is, using this tool, you can use… basically, it analyzed all the dependencies, figured out which instrumentations were…
auto-instrumented, and then brings you to this list to say, like, okay, if you use… if you were to throw the auto-instrumentation agent on this, the HTTP client will give you these metrics.
you know, the Hikari… the… you'll get this metric from the Hikari, instrumentation, and then there's spans, so… so yeah, so… and this is just very, very much a proof of concept and experiment, but it just wanted to demonstrate some of the…
the different metadata that we could collect, the way that we could use it, and then, some of the different tooling that we could give to users. Like, I see this, you know.
not in the topic of documentation necessarily, but eventually we could generate dashboards with this. There could be migration automation to say, you know, if you're migrating from 217 to 3.0, you know, these are all the things that you're going to need to change in your dashboards and tools and alerts and all that.
And so, to bring it back.
You know, there's a lot of functionality within that that maybe wouldn't apply to the dock site, I don't know, but…
I wanted to start the idea of, like, maybe some of these concepts of ways that we can answer these questions. Like, maybe it would make sense to move them into a more discoverable place, so I would assume the documentation site. I don't know, you know, like, this is like a React app, and I don't know how…
Technically, we would accomplish it with the current frameworks that we're in, but that's… I wanted to, you know, break the ice and start that conversation. So, so yeah, I'll pause there, but my idea is, eventually, I want to kind of pave the path for, like, a lot of these concepts are language-agnostic. Not every language, but JavaScript and .NET, at least, are very similar to Java in a lot of the same concerns.
So I would like to…
try and prove out a way that we can, you know, put together certain ways to document instrumentations and then make them more discoverable for users. So, yeah, that's… those are… those are my thoughts, and I'm interested to see what you guys think.
Yeah, Patrice?
Patrice 00:26:05 First reaction is awesome.
I love automation,
And I've been in documentation, documentation automation for quite a while now, and this is great, this is phenomenal.
Jay DeLuca 00:26:22 Thank you.
Patrice 00:26:24 the JavaSig has been…
in the lead, for a while. I think it would be great to integrate this. I took part of my summer to,
try and get more familiar with the ecosystem of tools that we need to make our websites work better, including React.
And seeing how… what sort of integration can we get with, you know, a Hugo-based website, and…
Anyhow, so I think this is great. I… it… so, it's not my area, not my field, but…
Like, not that level of detail, but the questions you put there seem, like, very, very…
prime questions that I would expect users would want to have.
I think your proof of concept
seems to provide very, very useful information in a compact way. I would love to see this integrated. Whether it gets generalized, I don't know, but…
I would certainly support bringing… finding a way to bring this… integrating this into the website somehow.
Even if only through a subdomain for the app.
And grow it from there. I think other SIGs will see the value and… but there will be legwork to be done to create the metadata file to make sure that…
But that would be their responsibility. But, I love… I love what I'm seeing, and I would support bringing this in
Sooner than later.
Jay DeLuca 00:28:03 Awesome.
Thanks for that feedback, Severn.
Severin Neumann 00:28:07 Yeah, awesome, awesome is, like, is the word of the day, like, it's hard to communicate the excitement about it via Zoom. But I try to describe it a little bit, so I'm not sure, like, how much, history you have on our project.
But, like, what we copied over from OpenTracing is the registry, right?
And there was always the idea of, like.
doing a better version of the registry, right? Do something…
that does something like that, right? That gives you a lot of metadata, like, and…
there's even a draft proposal in the community repository where I said, like, hey, I think you even liked that back then.
I, I just feel like there's a thumbs up with your GitHub handle.
But this was ever, like, something like… nobody had the resources for it, right? Nobody was, like…
We did a lot of incremental improvements to the registry, but never, like, hey, actually, this should look entirely different, right? We need, like, a…
a thing that looks more like NPM.js or whatever, like, where you can search that stuff, where you can, like, get
certain details, and there's some metadata and standards, and everything, and I know that the collector SIG has some metadata already, but we're not pulling this in.
So…
I… the moment, like, Tiffany, you shared this last week with us already as preparation for this meeting. I saw this thing, and I was like, yeah, this is…
this is what we were always looking for, right? For me, this is the way how our registry should be looking like, so…
I think the question I have more is, like, How can we… make this happen, in a way,
that it works.
for all the Sikhs and all the languages, right? That would be, like, then we could say, just like, let's throw out the existing registry and make that our thing. That's how I think about it, but yeah, I don't know.
Jay DeLuca 00:30:24 Yeah, and I like the idea… I think it's
it would be good for us to focus on Java for the initial implementation and work out some of the kinks and, you know, figure out what metadata we don't care about. But yeah, I do think that it could be generalized, or at least some of the concepts of, you know, at least be able to look at… even if the metadata or the
The attributes are different for the specific components.
you can still, like, look at them version to version. So, like, if I have this version of it, you know, what changed here? And… so yeah, so, like, I… in terms of, you know, how do we get this in, I…
I think the subdomain with a separate, you know, project is probably the easiest, maybe at first, and I don't know if… I don't know if there's value in getting it into the Hugo kind of framework or whatever, but, I was thinking, you know, the outcome of this was I'll open up an issue in the doc site, I'll kind of
put down all of my thoughts and ideas of the progress that I have, and what I think isn't needed next, and then we can collaborate on, you know, how to proceed from there. But, there's still a lot of work on my end in terms of
the Java, metadata, so I've… I've gone through… I'm going through every mod… like, there's over 250 instrumentations in that project, and I'm…
33% done going through them and analyzing them, creating the metadata, the telemetry interception and stuff. It's a bit of legwork, but, it's exciting to see it, you know, come to life, so I'm gonna continue working through that, and then my thought is, you know, to start, you know, interacting with you guys and figure out
what the next steps are to kind of push this towards the OpenTelemetry.io site, or subdomain, or whatever.
I don't know who raised their hand first. Patrice, you wanna go?
Patrice 00:32:18 I did. You can measure the level of excitement by the number of hands that are…
Severin Neumann 00:32:23 And we raise our hands, and it's just, I talk all the time, as we do it normally, and I'm like, I hold myself back.
Patrice 00:32:32 Just a clarification question…
I wasn't seeing that this would necessarily be a competition to the registry. I thought this was complementary to the registry, is that correct? Or, Jay, are you seeing this as replacing the registry?
Jay DeLuca 00:32:51 I… I'm not sure. I… I have…
I've gotten very little value out of the existing registry. I think there could be a place for it, maybe…
for, like, native instrumentations that we don't have the control over, or, you know, like, Quarkus or Camel that kind of do their own thing. Like, maybe there's a registry for…
I'm not sure. I've thought about it a little bit, but it seems to me that this could replace many aspects of the registry, but I'm not sure about the whole scope of the registry in terms of whether we should replace it outright or just move
Some subset of concerns.
out of it into this, or whatever. But we could certainly… continue that discussion. Okay.
Patrice 00:33:39 Is this… I'm asking, I guess, both…
From a designer, a site designer perspective, but also from a user perspective, if there are these two services.
Jay DeLuca 00:33:48 There we go.
Patrice 00:33:49 We'll want to be clear in terms of
where you want to go to get whatever answers. In the beginning, I would certainly value getting whatever you have up
sooner than later, so that people can give feedback. We'll just want to make clear that
Whatever issues are opened over the right repository so that they can be addressed.
Jay DeLuca 00:34:10 True, yeah.
Patrice 00:34:11 And agree that we… down the line, we can figure out what's left in the registry that's useful, or what's redundant, what can be pulled out, and…
Okay, thanks.
Jay DeLuca 00:34:22 Tiffany?
TH Tiffany Hrabusa 00:34:24 I kind of already brought this up to Che when we were speaking.
About this the first time, but I would be thrilled if we could bring in the collector component documentation through, this kind of tool, where
the metadata, the YAML files can still live in the core and contribos, which is what the developers want, but we're able to pull all of that information into the website through the Explorer, so that's just my…
Very excited future proposal.
Jay DeLuca 00:35:03 Yeah, and so just one little side note is, so I already have some automation in place. One I have that actually… so on the doc site right now, we don't have a supported libraries list, but we have a suppression list of all the libraries, and
I have automation that every night in the Java repo, it checks to make sure that all of our libraries exist on that page. And then, within the Instrumentation Explorer itself.
Every night it checks
the main repos for any changes, pulls it in, and then generates, and… because it's just a JSON backend, essentially, and so it just… every night it checks for changes, updates the enriched JSON, and then redeploys it. So,
Yeah, so we could keep all the source of truth alongside the code, but just have automation
That basically just consumes it, massages it however we need, and then, you know, posts it, so… Severin?
Severin Neumann 00:36:01 Yeah. I think my comments go… go in, like, the same direction, but, like,
I think if we can prove that we can add collector components, and maybe a second language, like, I don't know, let's say Node.js, for example, then for me, this would be proof enough that, like, this can easily supersede the existing registry, right?
I mean, we can even talk about how we can add native instrumentations to it, and if it's only, like, yeah, they exist, go to this website to get more details.
Or we ask them, like, hey, since you have hotel support already.
generate the following form of metadata, and we can pull it in and do something with that, right? I mean, but that's, like, that's something I would not worry about right now. So from a…
from a… from that perspective, I think the big question is, like.
and this is maybe also something I'm curious what Patrice and Tiffany and also Vitor, or Sophia as well, like, what do you think about, dislike?
Maybe it's worth considering to put this into its own repository.
And maybe we even drive… Through the official project.
channel we have in the community to say, like, maybe we need to…
rally people around that, and Jay, if you say, like, hey, I'm super excited about it, I want to lead this effort, I'm very certain there will people show up and say, like.
I'm very certain that Pablo and anybody else from the Collector SIG is excited about it. I'm very certain that we find some other folks from some other language SIGs to say, like, yeah, we want to plug into that, so…
That would be my proposal, that we say, like, yeah, this is something, like, very related to dogs, very related to sitcoms, but at the end, it's probably something that maybe… that's at least also how I always saw Registry Version 2, that this lives in its own place.
Eventually, and we maybe consume the data from it in some way or the other, but yeah.
Jay DeLuca 00:38:06 would you… would you recommend, so I don't know the process of getting, like, a new repo provision. I would imagine
part of a.
Severin Neumann 00:38:14 So what I will do, definitely, I will share this with the GC. I'm very certain that there's a few people that will get very excited about this as well.
And then, maybe we can talk about next steps,
via… via Slack, and see, like, what's the best way for… for this to push, or what. But what I'm asking you is, like.
Are you… Like, willing to… Push this forward, like, become, like.
if this turns out to be its own project, like, to be the maintainer of that, and say, like, hey, I really people around that. Because this is what every project needs at some point. They need one or two people that say, like.
I'm taking the lead on that. My employer is happy with that, I'm ever happy with that. I mean, you just joined Grafana, so I hope they are like, yeah, Jay, please do that. If not, we know some people at Grafana that maybe can help with that. So, yeah, just…
Think about that.
Jay DeLuca 00:39:15 Yeah, definitely, and so… so right now, I am in the process of putting together, like, a project proposal internally, and evaluating, and, like, this discussion is gonna inform that in terms of, kind of, the scope of different options. And so, I can't commit 100% just yet, but I am exploring the idea of
kind of making it, you know, taking the lead on it, and I am interested in doing that as long as…
you know, Grafana signs off, so…
TH Tiffany Hrabusa 00:39:47 I just had a quick question, for my own reference. I thought the registry included, like, third-party components, like, things that don't live in our repos. So, I don't know if we would want to lose all of that necessarily, but maybe I'm wrong.
Severin Neumann 00:40:04 I mean, I guess we can add it here as well, right? I mean, it's more about, like, the metadata model and how we… how we represent things in that tool, right? That's at least how I think about it.
Patrice 00:40:17 That's part of what I was thinking, and why I was seeing… I wasn't seeing the replacement, but it could be that the registry then becomes, atrophied.
And specialized in that use.
And so it's maintained.
TH Tiffany Hrabusa 00:40:33 Yep, yep.
Patrice 00:40:34 in its current form, or another form, or maybe integrated, but I would see that as secondary. I think
I don't want to take any wind out of your sails.
For this specialized and very useful addition.
And then to… we can consider third-party, packages later.
Jay DeLuca 00:40:55 I… What I… sorry, go ahead.
Especially since they already exist in, like, YAML files, so, like, it would be trivial to include them in some way, so…
Severin Neumann 00:41:05 Yeah.
I think if we really say, like, hey, this is, like, what we want, and at some point we want to
either limit, or even remove, or whatever, do with the current form of the registry, the easiest way is, like, go to the registry and put a big banner there and say, like, hey, look at this new shiny thing, right? And then slowly see how it turns out.
But yeah.
I said, I think for me, next steps, as I said, I will share this with a few other people as well, and then maybe we consider having this as a separate thing. Except, Patrice, Tiffany, I don't know if you think, like, hey, this should be part of the hotel.io repo.
But I suspect it's easier to.
Patrice 00:41:49 No.
Severin Neumann 00:41:50 is standalone.
Patrice 00:41:51 That's why I was raising my hand. Well, for two things. One is to acknowledge, definitely, I would see this as a separate repo. It will be easier to manage. I'm glad you challenged my assumption, or at least brought up the question.
thought, Jay, that you would be leading this, given that you're saying, for example, you've covered one, you know, 30… one-third of the libraries that you wanted to address already. So I think there's work to be done.
Quite a bit.
Still, so if you can continue to lead that effort.
And that's kind of… that's the feeling I got, and… but I understand that you'll… you'll be coming back to us to see if you can…
Indeed, lead that. So good.
Jay DeLuca 00:42:40 Yeah, and just for the record, I already fully intend on finishing the metadata project for Java. It's just the…
you know.
donating this upstream and getting it all, like, polished and all that is the… kind of the bigger project that I'm not sure how much of my capacity I'll know, but I should know that soon, you know, in the next couple weeks, I would imagine, so…
Patrice 00:43:02 Okay.
Jay DeLuca 00:43:02 And I do have aspirations to do it, so I do want to do this, so…
Patrice 00:43:05 Excellent. Maybe to fill in, I'd mentioned to Severin that
I was willing to champion, or at least be a cheerleader for the registry version 2 as a dynamic app. If this is it, which is part of the question I had earlier, which is, is this really meant to replace the registry in all its current aspects? If so, then…
I… can, see if… There could be bandwidth.
On my side, if I can be allotted time to work on this, and then maybe we can work together, I can help.
Jay DeLuca 00:43:42 I'll set up the registry and.
Patrice 00:43:46 Evolve the project, or support you as… as this is built up.
Jay DeLuca 00:43:52 Appreciate that. Fingers crossed.
Patrice 00:43:54 Yeah, so, Severin, in that sense, if I pitch it as… Registry version 2.
Hmm…
Severin Neumann 00:44:04 I would see it that way. I would not see, like… I mean, it's a… it allows us to search instrumentations right now, right? And if, Jay, if you say, like, hey, we can also add collector components, because, like, they do something very similar, I wouldn't at some point, click on a collector.
component and see, like, what telemetry is it generating, etc, etc, right? And then there's probably other tools that we maybe can represent in some way or the other, or not. Maybe we decide, like, hey, this requires
an awesome OpenTelemetry list on GitHub, and we just push it there, right? And say, like, hey, all the cool tools live…
In a different place, and this is dedicated to
like, collector components, instrumentation libraries, blah blah blah. Yeah, this is what the registry always should have been about. I'm curious, maybe, what Austin and some of the other people say that have been around at open tracing times, but that's at least my feeling about it.
Patrice 00:45:02 Okay. I'm starting to think that maybe that question I just asked isn't relevant. I'll see what I can…
Do you to pitch, for this feature.
Do you wanna… bring it up with Austin to see if he has any feedback.
Severin Neumann 00:45:21 Instead, I will share it with the GC in general, because I'm also curious what some of the other GC members say about it.
Patrice 00:45:28 Dead.
Severin Neumann 00:45:29 And then, yeah, we take it from there. Maybe at some point we even should share it in the maintainer's channel and get…
Very broad feedback on it.
Patrice 00:45:38 Okay.
Severin Neumann 00:45:38 But yeah, this is really like…
One of the most exciting things right now.
Patrice 00:45:45 So, thank you, Jay.
Jay DeLuca 00:45:47 Well, thank you guys. I mean, I've been working on this for months, and it's really, like, it makes me feel good to hear the positive feedback, so thank you.
Severin Neumann 00:45:56 But that's, like, what I said, right? I mean, we had, like, ideas around doing that, lingering around forever, and I was also like, hey, whenever I have time, I sit down and coach something like that.
Patrice 00:46:08 But never got to it, as you can see. So this is, like, what excites me about it. You took the lead and said, like, yeah, I built something, and you made it tangible, and we can take it from here, right?
Severin Neumann 00:46:20 Yeah, I said, we have some next steps, I will… I will keep everybody in the loop. We have another one or two topics, so maybe if we…
do the rest async, we can maybe quickly jump to… to…
Tiffany's topics. I can reshare my screen if you like.
I'm gonna, I'm gonna jump, but thanks, thanks everybody, appreciate all your input. I'll open an issue, and then, yeah, we can continue this ASAP, so… Yeah, awesome, thank you. See ya.
Jay DeLuca 00:46:50 Thanks, guys. Bye.
TH Tiffany Hrabusa 00:46:51 Thanks, Jay.
Severin Neumann 00:46:54 Tiffany, you had two more topics. There's also something on the Romanian localization, yeah.
TH Tiffany Hrabusa 00:47:03 Yeah, I… I actually put all three of those in there, but I don't have much to say about the Romanian localization, I just wanted to surface it that someone had… I think Diana has been asking about it, so I don't know if we want to move forward on that, but going back to the topic before,
not as exciting as the Instrumentation Explorer, and probably a bit more thorny.
We're having lots of problems with, the… Opentelemetry bought
collector release updates, and it's complicated because the collector has at least 3 different repos.
And they don't all have the same release numbers, and they don't all get included in every release.
And so…
Basically, the problem on the docs PRs is the link checking is failing because, those release pages don't exist for some of the artifacts.
it's hard to know… there's no rhyme or reason as to which piece is going to be included in which release, so I don't know if we can even
do automation anymore. I don't know if we just let the broken PR sit until the next release that passes. I don't know what the solution here is, but this is probably just a very initial conversation about how we approach this problem.
Severin Neumann 00:48:36 When you say 3 repositories, my understanding was this was less about the repositories and more about different components, like the collector-builder…
And, and, and some other things, or… am I… Did I misunderstand it, right?
TH Tiffany Hrabusa 00:48:52 They have core and contribos. Yeah. And then within that, they have the builder, supervisor, and then,
I think there's one other component, but I'm not entirely sure. But it's a combination of the two.
That there's different components, and there's different repos, and they don't always coincide with the same release number, or all get included in the same release.
I think.
Severin Neumann 00:49:20 And the references that we make, could we untangle them and be sure, like, which one points to what?
Or is this, like, too complex?
TH Tiffany Hrabusa 00:49:31 So, Patrice can probably speak better to this, but right now, it's a cascade function, right? We put the collector release number in the Hugo cascade field in the front matter, and that just updates blanket everywhere that we refer to the collector version.
we could probably, on, like, the builder page, or if there's a supervisor page, I'm not even sure, we could probably override that cascade somehow, but I'm not sure that that would even…
take care of everything. We could try it, though. Patrice, do you want to chime in?
Patrice 00:50:05 This has been an issue for a while, we've been burnt.
Before, and handled it manually.
I'm glad this is getting attention.
If our… if our front matter variables are too coarse, maybe we need to refine them.
Coming… answering your question in terms of is it automatable?
Well, clearly, we can detect
That's what the link… essentially, it's being pushed down to the link checker, and the link checker is then saying, hey, these artifacts don't exist. So we could…
do that.
earlier, just thinking quickly, off the top of my head.
If we had a rollback release version that we know exists, that could be a quick solution.
So at build time, we would actually check whether the resources exist, and then
create the appropriate links to the resources. So you'd have…
version X is what we think most collectors' packages are at, or resources are at, and the fallback would be
version Y that we know it has resources… no, no, okay, that won't work. Anyways, so either refining the front matter variables seems like one solution.
a fallback like this, which would need closer analysis, or we just drop the automation and have the collector folks submit PRs by hand, and make sure that the build
Has no, link check failures.
Probably a deeper dive to find out what the packages are and how easy it might be to have different variables per package or resource or whatever. That might be the way to go.
TH Tiffany Hrabusa 00:52:18 Yeah, I think… I think that might be…
Because I know the few PRs that I've seen recently, it was…
I think first it was that the…
release did not include the builder, and then later on, the release only included the builder. So, I think maybe if we focus on the pages about the builder, the supervisor, those two artifacts, that might at least diminish the frequency of these issues, and then
you know, if we see one-off things coming up here and there. We can…
Address those later if we feel the need to, or, you know, if it's infrequent enough.
I will also say that the collector, SIG, is struggling with their own release process right now. I attended the meeting this morning, and there was a lot of frustration.
express about how things are going. We saw the PR that came in with the collector release nightly.
That was a mistake, it shouldn't have happened, and…
there's lots of stuff going on there. I don't know that anything will change from an infrastructure point of view. I think their workflows might change, but I think we will still be dealing with multiple artifacts and multiple repos and multiple release numbers, ultimately.
So,
I will not have time to deal with it until I'm back, at the end of September.
So… I think I've already created an issue.
Patrice 00:53:52 The one we're.
TH Tiffany Hrabusa 00:53:53 If anybody needs. Yeah, yeah, yeah.
Yeah. Sorry, I've got street monitors.
Patrice 00:53:59 That's okay, no worries. I just wanted to make sure that was the… The red one. Yeah.
TH Tiffany Hrabusa 00:54:05 And I'll add the quote that I put into the release notes. If it's not in the issue already, I'll add that too, just for context. That quote came from Jad, who, is very involved in collector docs, so, she gave a very good explanation of
what…
The problem is, and that it probably has to be fixed on the docs side, because it's way too complicated to fix on the collector side.
when I get back, if no one has touched this, I will, work with her to figure out exactly…
How we can override, certain pages within the collector docs, maybe, that are the frequent offenders.
How does that sound?
Severin Neumann 00:54:52 Yeah. I mean, since we only have 6 minutes left, 5 minutes left, and since you're going off
on a break. I think to answer your very initial question, I have no issue with, like, those PRs breaking right now, right? I mean, we did the same with SPAC and SEMConf at some point, like, there were some breaks going on, and nobody of us had bandwidth to fix that.
nothing of that is as urgent that we say, like, hey, this has to be fixed tomorrow, right? I mean, the collectors, if they think that's that urgent, I mean, then they can assign bandwidth to it themselves and untangle it.
I think… I said this before, I think the…
the variables, how we have them today, I always wonder, like, if we should, like, take them out of the front meter into, like, a YAML file or something like that.
also because they sometimes make issues with the localizations, that's maybe a separate discussion we cannot solve in 4 minutes. At least when I try to restructure
the zero code instrumentation back to auto-code instrumentation.
things go haywire, because, like, Java has a lot of variables at a lot of places.
The other thing where I'm not sure, I thought that we picked some of the versions out of the registry. So yeah, we definitely need more time to analyze that. I think that's the long answer to that. So, short answer, don't worry about that while you're away.
in the worst case, really, with it breaking, and Patrice or myself, or any other maintainer can tell the collector maintainers, yeah, we…
Cannot fix this right now, so if you want to have this fixed, do manual changes.
And then we slowly should take some closer looks at end of September.
Because they're main, concerned with their own release problems right now, so we probably just, like.
In their blast radius right now. So, yeah, that's… that's my answer on that.
TH Tiffany Hrabusa 00:56:58 Okay, I have one quick ques… maybe not quick, but hopefully quick.
Patrice, I remember you giving us a script in the past that allowed us to force the link checker to skip over, I think it was LinkedIn URLs because of something. Could we run a similar script on these PRs to force it to ignore the links
That are breaking because the artifact doesn't exist, and then we could at least update the other
Links, or is that not worth…
Patrice 00:57:30 We can, but then we'll face the issue of a user clicking on that link and then opening up
An issue to say, hey, your links are broken, fix it.
TH Tiffany Hrabusa 00:57:43 Oh, I see.
Patrice 00:57:45 So the link checker will say, okay, I'm not checking those links, and it'll happen to be to a resource that doesn't exist, so we have an end user who clicks on that, says, hey, your site has a broken link. So we're… it delays… it delays
our knowledge of whether the resource exists or not.
TH Tiffany Hrabusa 00:58:06 Okay.
Moving on, then.
I don't know if we want to talk about the Romanian localization, but Diana seems eager. I don't think that, she has found anyone…
To, be, like, a co-reviewer or a co-maintainer with her.
Severin Neumann 00:58:26 I think that's… I told her, like, raise the issue, create the PRs so we can rally people around it. Unfortunately, like, there's no Romanian glossary right now that was, like, a good source.
people recently. I think another thing we can do is, like, do some…
social around it, that that would be the next thing, that we maybe send out just the LinkedIn, whatever, post, and say, like, hey, are you a Romanian speaker? I think my only question is, like, Deanna seems to be…
already, like, well embedded in the CNCF universe and hotels, so I think we could treat her as, like, the mentor to that, and, like, the…
The owner of that, or do we think, like, we need some senior person to look into that?
Like, like we did with the Ukrainian, where we have Ehor.
to… to steer that a little bit. I think we did this with a few of the last languages.
TH Tiffany Hrabusa 00:59:24 You're asking whether…
Severin Neumann 00:59:26 Go ahead. Yeah.
TH Tiffany Hrabusa 00:59:28 I think if we're being, equitable, then we need two people, at minimum, to… to start.
Severin Neumann 00:59:35 No, no, but recently we said, like, we not only need two people, but one person also should be, like.
Oh.
Patrice 00:59:43 lease.
Severin Neumann 00:59:44 senior, in some sense, of, like, either being already a member of the community, or maybe, like, CNCF Glossary, or…
Oh, we could check with Kubernetes. I'm not sure if they have a Romania localization, I can… we can check that.
Patrice 01:00:00 I don't know. I defer to you if you think she would… this person would be senior enough, then…
I deferred.
Severin Neumann 01:00:08 She's already, like, a contributor to the hotel project.
yeah, but not a member yet. I think she's, like, a… How do you say that?
and CNCF Ambassador, or something like that.
Patrice 01:00:27 She's embedded in the ecosystem, I think that was what I wanted to say, but…
Severin Neumann 01:00:32 Romanian…
Patrice 01:00:36 at least from GitHub, you… pulling up her page doesn't show necessarily that much.
Severin Neumann 01:00:42 Yeah.
Patrice 01:00:43 So…
Severin Neumann 01:00:44 Yeah.
Patrice 01:00:45 Let's still be on the lookout for somebody… Senior?
She might, she might just have trouble recruiting support for the localization, so…
Severin Neumann 01:00:59 It's on our radar, let's see how things evolve, if she can find some support, if…
Patrice 01:01:05 And I agree with what
You suggested, which is what we do most times, is to post in Slack and elsewhere.
Ask them. Yeah.
Severin Neumann 01:01:15 Yeah.
Yep.
I need to drop now, I have more or less a hard cut, unexpected.
Patrice 01:01:22 I'm gay.
Severin Neumann 01:01:22 I would have loved to talk about the proposed architecture for the collector. This looks awesome. Just to add that, like, another thing I was excited about seeing today. It's like, I don't know, Tiffany, you're away next week, so maybe we can rally around it when you're back.
TH Tiffany Hrabusa 01:01:41 Yeah, I'm out for 2 weeks, so I will miss the next iteration.
Severin Neumann 01:01:45 like…
Or we do it ASAP.
TH Tiffany Hrabusa 01:01:47 Yeah.
Severin Neumann 01:01:48 When you're back.
Yeah.
TH Tiffany Hrabusa 01:01:49 Yeah, I think, yeah, it'll probably have to wait until I'm back, because I won't have to… I'm leaving Friday, so I won't have time between now and then.
Severin Neumann 01:01:58 But it looks like… I like it very much. I reviewed it, and I was like, yeah, this is a really good structure.
So I would… would be eager to see that.
TH Tiffany Hrabusa 01:02:07 the collector folks were really happy with it, so I think we're safe moving forward. But yeah, if anybody wants to take a look, and I'll add, there's a Slack thread that I put into the collector channel.
Severin Neumann 01:02:19 You know?
TH Tiffany Hrabusa 01:02:19 You can… while I'm gone, if you have feedback on it, you can always add it there, and then I'll… when I get back, I'll…
Severin Neumann 01:02:26 Yeah.
TH Tiffany Hrabusa 01:02:27 go through all of that. Okay.
Severin Neumann 01:02:29 Yep.
Thank you.
Patrice 01:02:33 Thank you, everybody.
Severin Neumann 01:02:33 Bye-bye.
TH Tiffany Hrabusa 01:02:34 honey?
Patrice 01:02:34 See you next time.
Sophia Solomon 01:02:35 Betty?
Vitor Vasconcellos 01:02:36 Thank you.
