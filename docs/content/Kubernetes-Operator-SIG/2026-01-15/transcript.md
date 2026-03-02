SIG: Kubernetes Operator SIG
Date: 2026-01-15
Duration: 61 minutes
============================================================

## Zoom Recording Transcript

**atoulme** 01:11 Thank you, guys.
**Mikołaj Świątek** 01:16 Hello.
**atoulme** 01:18 Hey.
**Mikołaj Świątek** 01:20 Been a while. How was your, how was your, Christmas break?
**atoulme** 01:26 That's good. Little rainy.
How about you?
**Mikołaj Świątek** 01:32 This was pretty good. I actually had something like a real winter. Not for Christmas, exactly, but a little bit leisure. We had a pretty heavy snowfall, like, heavy enough that it was, like, a…
An impediment to logistics.
Let's call it.
In some places, around the country.
Well, it was nice. The weather was kind of, like, nice and cold. Right now, it's awful. It's awful. It's not as awful as…
It's not as awful as yesterday, because yesterday it was freezing, it was below zero Celsius, but it was also raining.
**atoulme** 02:12 Mmm.
**Mikołaj Świątek** 02:13 You know, the rain would fall down, and then become, you know, this layer of ice over literally every surface.
**atoulme** 02:22 Yep.
Yeah, when I say it's cold here, it's usually 15 Celsius or something.
**Mikołaj Świątek** 02:28 That's cold.
**atoulme** 02:29 Wow.
**Mikołaj Świątek** 02:30 Wow.
**atoulme** 02:32 It gets down to 4 degrees at night, and there… we actually get emails that it might freeze, so they actually send us, like… the county of Santa Clara sends you an email, like, you need to prepare because you may… it may freeze, you need to protect your fruit trees and all that.
I will see people, like, putting, like, stuff on top of their fruit trees so that they can survive.
**Mikołaj Świątek** 02:53 And here I am, getting down to minus 20 Celsius at night.
In the past few days.
**atoulme** 03:02 I would not survive that.
Yeah, no.
**Mikołaj Świątek** 03:06 It's easier to survive that than it is to survive temperatures over 40. That's true. Celsius, in my opinion.
**atoulme** 03:13 True.
You get used to it, too. It's just, anyway…
**Mikołaj Świątek** 03:19 Yeah, there is this thing, there's this, I think it's called the Wim Hof Method, where you train in a particular way, and you become, like, very resistant to cold, even, like, undressed.
And you see people doing that. They're, like, in very snowy conditions. They hike up mountains just in, like, their light training clothes, like, bare-chested, and just in shorts.
**atoulme** 03:50 Well, no, it's a good hobby, yeah, sure.
**Mikołaj Świątek** 03:53 Yeah, I mean, it's supposed to be healthy for you, same as taking very cold baths. It's supposed to be healthy.
Am I the only person? By the way, I don't see anything on Hacker News, but GitHub has been throwing a bunch of 500s for me.
Recently.
Am I the only person experiencing that?
**atoulme** 04:16 Good news this morning.
**Benedikt Bongartz** 04:19 Works. No. I couldn't push…
**PL Pavol Loffay** 04:21 So…
**Benedikt Bongartz** 04:21 Today, But, aside from this.
**atoulme** 04:24 So.
**Benedikt Bongartz** 04:26 I was thinking it's an issue on my end.
**atoulme** 04:29 I know, you're right, there's, Status GitHub says that it's down.
**Mikołaj Świątek** 04:34 Oof.
**atoulme** 04:44 Okay.
**Mikołaj Świątek** 04:44 At least they have a status page that says something.
You just won't.
**atoulme** 04:54 You have multiple status pages, they do different things.
**Mikołaj Świątek** 05:00 I did have a… did Jacob say he wasn't gonna make it?
Yeah, he said.
Might not make it.
**atoulme** 05:10 Maybe new job.
**Mikołaj Świątek** 05:16 Mmm… Yeah, on the… I just saw your question on Sargent one, and I think…
Like, where you can do releases as an approver.
**PL Pavol Loffay** 05:28 Yeah, bro, as well.
**Mikołaj Świątek** 05:32 The only thing that you need, like, you need a maintainer to merge your pull request, but after that, you can actually, like, you could create a draft release, and you can undraft it yourself later.
When you are.
**atoulme** 05:44 I don't see why I wouldn't pull my weight and help out. That's the only thing, is like, if you left me out for…
out of… PT or something, just don't. That's the job.
**Mikołaj Świątek** 05:53 I forgot.
**atoulme** 05:55 Okay, so.
**PL Pavol Loffay** 05:56 I want you there.
**atoulme** 06:00 I will add myself to the rotation then. I mean, you have a… the project has a decent rotation by now, it's just, like, 6, 8 people or something?
But why not, right? It helps. And I think I need to know a little bit more about how that part of the project is done. I never spend the time, so it's a good… it's a good opportunity to learn more.
**Mikołaj Świątek** 06:20 Yeah, it doesn't do anything exceptionally interesting. There's, like, one… there's some annoying bits that you have to do manually, and there isn't really…
A very nice way to automate them.
But other than that, you just kind of, you know, generate the changelog, submit a pull request, it gets merged, that creates a draft release, and you go and, you know, undraft the release.
**atoulme** 06:46 Good.
**Mikołaj Świątek** 06:46 There is something that I think we're pretty bad at, even though it is actually… it does actually say in the release notes that you should do this, which is that you should go to the Helm charts and update there as well, afterwards. So, that actually might be automatable.
reasonably, because that doesn't actually, like, require you to do anything other than running some commands over in the home charts repository.
**atoulme** 07:11 That's good, good to know.
But it's kind of stuff, like, if I don't get to experience it, I don't… I don't really have a say about how it should be run. I'd love to at least,
play that forward.
Okay, I'll end myself to the release rotation. On that note, I'm having a healthy debate with my engineering on that.
The release notes that we make for all distribution of the collector tend to be very,
complementary to what you can see from Contribin Core for the collector. So we actually go out of our way, and when we make a release note, we say, here's the stuff that we're doing in our distribution, and here's the stuff from Contributor, stuff from Core.
And for the operator, you're falling inside the same category of problems, where, frankly, the operator is just a subset of everything that you ship.
you're shipping new versions of the Node.js SDK, you're shipping a new collector, and all that. And, does the operator, in its changelog, or in its release notes, do you have some editorial capacity to maybe add…
Information about the changes that are important underneath.
Or, in a sense.
**Mikołaj Świątek** 08:22 It's like, yep.
**atoulme** 08:23 Trying to hide that, but…
**Mikołaj Świątek** 08:25 The… so what we do is, with every release, we publish, like, a listing of our subcomponents, and there's, like, a link to all the releases underneath.
I don't think we are able to… or maybe differently. We do actually do this for the collector.
As in, not necessarily even… Talk about changes, because it's not clear
what specifically we should, like, we're not gonna just put in the whole changelog, but if there's, like, a change that we actually… that is in some way a breaking change, then it's not so much that we publish
the… that we pointed out in the changeup per se, but usually we actually fix it in some way, as in we, like, add some upgrade.
**atoulme** 09:16 Understood.
**Mikołaj Świątek** 09:18 There's a migration that does it.
**PL Pavol Loffay** 09:20 The idea was that we will shield users from breaking changes in the collector.
But we don't do it forever. There is many breaking changes go through, and we don't notice them.
And I think we do a fairly bad job of identifying those breaking changes.
**atoulme** 09:44 Okay, so if you upgrade the collector, you are…
**PL Pavol Loffay** 09:47 That there is a high chance that a user will run into some incompatibilities.
**atoulme** 09:53 Do you, I just had an idea. Do you think the changelog of the collector should actually call out which portion of the changelog of a release should be added to the downstream projects?
Rather than putting this on you, should it be the collector's job to make sure, hey, operator, when you make a release, you should also copy this part of our changelog, because this actually is going to be… is significantly breaking the experience downstream.
**PL Pavol Loffay** 10:21 I think every kind of breaking change…
**atoulme** 10:24 That's true.
**PL Pavol Loffay** 10:26 It's like, it's not only enhancements, but all the braking changes, I think, should be…
Signalized to all the consumers.
**atoulme** 10:35 Yeah, okay, well… Okay.
**PL Pavol Loffay** 10:38 Actually, that's a fun… I was… today, I was looking at the changelogs in the hotel.
And… let me share it with you.
GitHub doesn't models.
**Mikołaj Świątek** 10:54 Yeah, you know, where, like, we can't have a meeting. It's, you know.
**Benedikt Bongartz** 11:00 Give it a few refreshes, then it works.
**atoulme** 11:03 Here it is.
**Mikołaj Świątek** 11:05 My view of this is that if the collector published this, then we would republish this.
Okay. In, like, a generic, generic braking changes section, I am…
Maybe we could, but I am, like, very skeptical, in general, that… Like, if somebody doesn't actually…
check the collector changelog themselves, I am kind of skeptical that they're gonna check the operator changelog to begin with. Like, I'm not sure if I.
**atoulme** 11:41 Yeah.
**Mikołaj Świątek** 11:42 the group of people who look at the operator change log, but don't look at the collector changelog when they're upgrading, I don't know if that group is very big. I'm not sure. Maybe as for a file, maybe it's just WAR file to do it, because…
Having, like, information propagated closer to, like, the place where you ran into a problem for someone who's trying to troubleshoot is just…
more useful, right? If they have some kind of problem. But usually, if you do an upgrade of the operator, and then your collector fails to start, and it tells you about some… something in the config, you're usually gonna go and look at what happened in the collector, I think.
**atoulme** 12:27 Yep.
Yeah, amazing.
**PL Pavol Loffay** 12:29 was it.
**atoulme** 12:30 Yeah. Duh.
**PL Pavol Loffay** 12:32 This was interesting to me. I was looking at categorizing the… the changes in the collector-collector country.
So this is for the… This is for the country.
We have 56 enhancements.
12s.
Breaking changes.
the API change log for the country, it's like 58 breaking changes.
**Mikołaj Świątek** 12:58 I mean, yeah, but API… but API is just… is… is for component, development, right?
**atoulme** 13:04 For Contrib, too, because contribute's supposed to be a leaf and does not have libraries that it exposes that much, and actually those breaking changes were me telling the developers, hey, you've been exposing a bunch of APIs, you should not.
And, we've done a lot of cleanup, so the other thing is, like, there might be a bump in your… if you were to chart that over time. Not saying it's not nice, like, this is not cool, right? I'm just saying, yeah, it explains a little bit. For the breaking chain…
**PL Pavol Loffay** 13:31 If someone.
**atoulme** 13:31 Corn, that's a lot.
**PL Pavol Loffay** 13:33 Yeah, for people extending the collector and, like, building their components, I heard many times that there is so many breaking changes.
**atoulme** 13:41 This is the collector core, this is not the API, this is the end user.
**PL Pavol Loffay** 13:46 Change log, it's like 40% are breaking changes.
**atoulme** 13:51 Yep.
**PL Pavol Loffay** 13:52 This is the API, again, like, 40%.
This is the semantic conventions…
**atoulme** 14:01 Yeah.
This is good stuff.
**PL Pavol Loffay** 14:02 Showlines.
**atoulme** 14:04 I will, I will, I would like to refer that. It's refund.
**PL Pavol Loffay** 14:09 And, yeah, this is the MCP proposal, I think. Antoine, you've seen it.
**atoulme** 14:16 Yeah.
**PL Pavol Loffay** 14:17 But, like, the idea is that we want to enable open telemetry to be used with agent workflow.
And the good stuff, like, one of the goals is to…
make it easier for people to upgrade and understand OpenTelemetry.
And… We want to encode all the config Configs across versions.
**atoulme** 14:40 In the…
**PL Pavol Loffay** 14:42 in the MCP with the changelogs as well, so you can ask the AI agent to
Highlight breaking changes across the versions.
So, for instance, you are on hotel 0130,
and you want to upgrade to 140, it will figure out which components you're using in the config, and which, which configuration, actually, of those components.
**atoulme** 15:09 Fair enough.
**PL Pavol Loffay** 15:10 Find out which configs are deprecated.
And how you should upgrade.
**atoulme** 15:16 Yeah, I hope… I hope this tool is not absolutely needed moving forward, because that's just reflective of our own failures, in a sense. I know you're trying to fix a real problem, but…
Yeah, okay, cool. Actually, this is a good segue, because I wanted to bring up an issue for the SIG, in… related to configuration, and it's an issue that's been open against the operator repositories.
If you want to take a look at it, I will post it.
And I would like to just offer some context of why this issue was opened, just to understand where this is coming from.
And I don't really have a say about…
But it's about that much. Yeah, here it is, 4607.
So, this is an issue that's been opened by a guy called Jack Berg. If you haven't had a chance to work with him, he's a member of the TC. He's also very active on Java, and Java…
config, and he talks about it a little bit, like, in even not just JRConfig, declarative config.
I think I've had heart-to-hearts on this call before with you all, to understand better where you're coming from. And, you know, I've identified a number of things. One is the project is not particularly happy to be managing SDKs and the packaging. That has never been the operator's mission to do that, but you had to because
well, you need to get somewhere, and they're not going to provide the Docker images, so you did, and now you're married to that, right? And the same thing goes with configuration and things like this, because you had to kind of expose that. What Jack is saying is, this is great, what you've done.
But moving forward, what I would like to do is to have this declarative config sig to finally provide a layer of configuration that works for all SDKs that will be managed outside of the operator into its own lifecycle as the declarative config.
And then, when we come in, we would like to be able to work with you all to kind of make that part of the CRDs that are going to be exposed.
And that's the short of it. The longer discussion is, the reason these come up.
Yeah, so he's… he's kind of reflecting on the managed RFC, which, you know, this is this in-progress thing that we just need to keep, like, actually finish.
I'm pretty impatient about this. I want us to be done with it, because I'm like, I can feel the gold right there, let's go, but we're not able to get the resources now, Gina is too busy, we need to get back some overtime on this.
Jack is the TC liaison for another SIG called the Injector SIG, which is responsible for building a mechanism to allow to inject instrumentation SDKs into running processes as part of the initialization using a preload.so hook.
The injector C started with a donation that was made by Splunk as C code, but very quickly, that C code got ditched, because it was just very simple, like, just applying some environment variables if they were not set.
Instead, they're now using a ZIG library, which works in Alpine and Libsy environments, which is great. That's the presentation that Mikile did last year at KubeCon EU.
And, this is now code complete, right? So we're thinking, like, $1 type discussion now.
And the next objective of that SIG is to take the injector code and to start to see how to apply it to the operator to replace some of the functionality that the operator is currently providing with the SDK.go file, for example, where you're doing a lot of manipulations of the pod.
Instead, this manipulation would now consist of injecting the ZIG library into the container, and let it do its job at the level of the process inside the container in a clean, uniformized manner.
We've also started to target host-based solutions, so this Z code can be installed as an RPM or Debian package.
And we're running into the exact same problem that the operator has, which is that if you package
this little component into an RPM at Debian, that's great, but now you need all the SDKs, right? So, you're going to have to package them, too.
well, now you're maintaining them. Now, every breaking change of them, you have to explain in your changelog, and that becomes kind of a running, a running discussion.
So there is also, separately from this, a discussion in community, or no specification by Michele, who wants to kind of have a, dependency graph of RPMs that would be deployed by different… just telling you the whole thing, right? So you can… it's not really related to the operator at this point, but…
Michael is thinking we should have a RPM called OpenTelemetry, and that RPM has dependency to the injector, has dependency to the SDK for Java, SDK for Node.js, and whatnot, and when you do APT install OpenTelemetry, or YAM install OpenTelemetry, you get the whole
OpenTeametry ecosystem installed on your box, no questions asked.
So, for the operator, it would be kind of also a good way to kind of help reduce some of the maintenance and the running cost of running all those things. And
that's kind of where we are. I think, Michael and his team have already deployed this in the Dash Zero operator, and they're looking to upstream this whole method over to the operator as a…
So, you know, it's not going to be, like, replace wall cell everything, but add it as an alternative at first, and then see if it fits the narrative of the operator.
So, every discussion we've had on the injector-seq turns into big philosophical discussions about what to do with packaging for open telemetry.
and how to help with some of those SDKs.
who are completely ignorant about some of the limitations that they have. One thing Mikli likes to point out is that the Python SDK is very limited when it comes to exporting OTRP data. They don't support the HTTP JSON approach, meaning that you depend on protobuf, which means you're bringing a lot of library with you, which…
creates all sorts of tension to instrument applications with Python, because protot libraries bring their own dependencies, and then before you know it, you're having issues when you're instrumentation.
So it's kind of nice that we're identifying, like, downstream cases for that, but the injector is unable to kind of pass the buck down to the Python SIG. We have to kind of physically go to the Python SIG and start to get involved. So…
Okay, that's just a lot of feedback. You should read this feedback when you have the time. I will try to respond as well. I think there's too much in that message, he's sending a lot of his signals.
And I would like Jack to come to this SIG and talk.
And I invited him to do so, but I know that his time is limited.
**PL Pavol Loffay** 22:23 I, I think, Antoine, this, request is really related to…
To this ticket, to reuse the.
**atoulme** 22:33 Love you.
**PL Pavol Loffay** 22:34 config in the instrumentation CR. I actually started working on it. There is a pull request to introduce V1 Beta 1 instrumentation CR that embeds the SDK config.
It's… it was a draft, it's fading CI now, but I will continue…
working on this, and I would appreciate someone if you could dedicate some of your time on it.
**atoulme** 23:02 Yeah, okay. Yep, if you can connect the wagons on this one, because I don't think Jack knew about that, and I don't think I knew about that either. So, if you connect all that together, definitely we can… I'm happy to put some time into reviewing.
Fair enough.
**PL Pavol Loffay** 23:19 Actually, I thought that you opened this one, but it was.
**atoulme** 23:23 no.
**PL Pavol Loffay** 23:25 Who's dated?
**atoulme** 23:26 Yeah…
**PL Pavol Loffay** 23:28 And maybe where we should kind of think is, like, he's referring to the managed CR, but I thought that the managed CR is mostly for the collector, or at least that wasn't the initial scope that you had in the proposal.
**atoulme** 23:42 Managed CR was like, let's not give you any options whatsoever, and we pick for you. So, we're going to install everything, and we're going to not give you any choices. And it's interesting, because, actually Benny took that feedback to heart, and…
Gina, you know, she kind of, at some point, she, she fell off the true and narrow expression of the RFC. The RFC is like, no options. No options. Just install this, it's… your OpenShift cluster is now, you know, completely observable, and we don't let you do any changes.
And… and Gina felt, like, sometimes she's like, I can't… no, let's… let's just open it a little bit, like, I'll just say metrics, traces, and logs.
Unabled, yes, no. And Benny's like, no, no. Antoine said, no, you cannot have any options in there. So she's gonna remove that, and thank you, Benny, for that. Interesting, like, reinforcement of the message here.
And then, the idea would be, we try it with actual customers. Who are asking for this?
And we see if they like the… what we're selling them, like, if they like the poison that we're giving them. If they have any feedback, such as, oh, actually, I wanted my 50 different toggles and booleans.
Okay, let's have… let's have a discussion.
I think what Jack is saying is, like, oh, this is… this is really interesting, because I can… I can draw on this surface. Because you offered no configuration options, I can come in with my configuration, like, whatever you've done before, it seems like you're doing…
Like, a whiteout of everything, and you're starting anew on top.
Before you add any toggles or configuration, please consider my approach of declarative config.
**Mikołaj Świątek** 25:28 I am… I'm kind of… I'm looking at this, I'm reading for it right now, because I haven't… I haven't noticed it.
**atoulme** 25:34 Yeah, that's fine.
**Mikołaj Świątek** 25:37 Hmm, so… I'm wondering to what extent Jack is actually talking about… the…
manage CRD specifically, and to what extent he's talking about configuring individual instrumentations. It seems like he's talking about both of these things at the same time, to an extent.
And… and I wonder… I wonder which part of this he considers the more pertinent part, let's say. Like, is the more pertinent part that you should be able to configure an instrumentation using the…
using the config as per the spec, as defined in the spec, or is the important part that you should be able to do it all for the whole cluster in one place, right? Because those are…
related, but not… but independent. Like, we can do one or the other independently, and like Pavel… Pavel is already doing it for our existing instrumentation resources, which aren't so convenient, right? You have to actually manually create them and start annotating stuff.
But we can absolutely, and we do want to, if we can reasonably well to… to use the spec there as well.
We would really… I would really like to do that. I hate environment variables increasingly. And it has caused us some amount of pain. Like, we… I think, in terms of stupid bug fixes, the…
Oh, how are environment variables set in a… injected into, like, a given pod from the mutating webcook for instrumentation? I think that's, like, the highest churn.
part of the project. And it's like… it seems simple, but we actually tried to go through, like, what is actually said where and why, and under which conditions it is. There's a lot of it.
But I'd be very happy to just create a configuration file, and be done with it, and not think about it. And think about it, right?
**atoulme** 27:53 So what Jack wants, I think, ideally what he would like is that we create a config file, we ship it inside the container using whatever means, and then the injector does its magic, and then everything just is no longer the operator's purview.
to really care about that Boolean thing or all that. It also allows us to test this outside the operator, so that when the operator adopts this method, it has a high confidence that it's going to work, because it's been tested in isolation elsewhere.
Okay, you know what, I think we're all aligned, and I really appreciate the work that Pavel is doing, because that's exactly where Jack wants to run.
Let's, jack is giving us a bit of momentum, so it's also great to get some attention from the TC on this, and this, if we pounce on this and we do this for the instrumentation CRD, it will definitely help also Jack with his declarative config thing, because he's trying to make it so it's useful, and I don't think he's got very lucky in the past to get… like, you can feel it in the discussion, it's like.
Been working on this for 2 years.
Don't have much to show besides a YAML file.
Would love to see some adoption.
You know, it's kind of harsh out there.
**PL Pavol Loffay** 29:03 Are the SDKs already today supported already?
Like, the joy.
**atoulme** 29:06 Oh, yeah, that's a very good question.
**PL Pavol Loffay** 29:08 interest.
**atoulme** 29:09 So, because Jack works in the Java SDK, the Java SDK somehow is better than others.
And then there is, I think, maybe some work in .NET would be next.
And then there's a cliff.
That's what I'm understanding. I think with Node.js being third, and then there's down the road, like, even Python not really getting into it, it's just starting to unvar. Oh, you also mentioned the Go SDK is actually much more mature than others.
**Mikołaj Świątek** 29:36 Does the Go SDK support the config?
**atoulme** 29:40 I think this is what he mentioned. Keep me honest here, but…
**PL Pavol Loffay** 29:43 Is there, like, a place where I can check, like, How it's supposed Trustee Boards.
**atoulme** 29:49 We could ask Jack in that.
**PL Pavol Loffay** 29:52 I think that would help, because this will be a blocker for us to actually roll it out, right?
**Mikołaj Świątek** 29:58 Yeah, like, if they don't… if not everything that we do support it, we're going to have to, like, support both paths. That's gonna be annoying. Maybe it's not gonna be that annoying.
I'll have to say… we'll, like, we'll have to see how it actually looks in practice. Like, in an ideal world, it should be just completely two… almost completely separate club paths.
In this respect.
So, so maybe it would be fine.
**PL Pavol Loffay** 30:27 Maybe we can as well, like, In this new…
Approach, use the injector from the get-go.
**atoulme** 30:37 If it's ready.
Yeah, exactly. So, in a sense, it's like, you're washing your hands of this, this is an injector problem, you're going to allow the injector to play into the CRD, to try out as an alternative.
And you might not even need a different version of CRD for this, or however we want to try this out as a feature gate, or, whatever. Doesn't matter, right? It's just, we need to kind of see it come together, and then, see how it plays out.
**Mikołaj Świątek** 31:08 Like, that is, like, a major question for me, because I don't think actually using the injector, in terms of, like, the changes to the operator, I don't think that's going to be very complicated. It's going to be, like, delete some stuff, or just not do certain things. Potentially a more complicated question is…
do we use the injector for our existing instrumentations? As in, do we, like, quietly do a quiet migration, maybe behind the feature flag, maybe behind, like, an actual config field in the CRD? Like, but eventually, our intent is to have our current instrumentation CRDs use the injector underneath, like, we treat it as a implementation detail.
kind of change? Or do we actually want to expose this idea to users and create a new, like, explicitly a new method of injection? Because it might make a difference, right? The last time, I think Ricard…
Last time we talked about this, I remember, like, for example, the "-0 injection, the way it works is that it has to have all the instrumentations in place, right? And our images don't work like this. Our images are per language, and it…
I don't know, to me, that makes kind of a difference, because…
if you're injecting… like, maybe it doesn't, given that Dash Zero actually does this, and they have a bunch of customers doing it, so maybe it makes no… it's fine. But to me, if you're, like, putting something in the… in the hot… like, in the startup path of…
any application that is instrumented, basically, right? Because before that application can start, you actually have to do the instrumentation in the container stuff before it can actually start. Like, how big that instrumentation container is does make something of a difference.
**atoulme** 33:03 It'll… I don't really have answers for any of this yet. I think…
**Mikołaj Świątek** 33:08 I don't expect them, I'm kind of… I'm not trying to put you on the spot, and you don't want… well, decide, decide, tell me.
I'm, I'm kind of more…
thinking aloud here? Yeah, no worries.
**PL Pavol Loffay** 33:25 So many open questions for this. But on Monday, there is the InjectorSeek. I think I will join, and kind of… I would like to understand where they are, and if there is anything we could start, maybe.
Consuming and experimenting with.
**atoulme** 33:40 Just be aware that Monday is off in the US, because it's MLK Day, but…
I think the SIG meeting will happen anyway, because we have a number of people outside the US who happen to be there. So right now, we're not looking to,
We're not looking to, to, renew… take that off, to cancel that meeting.
Okay, after…
**PL Pavol Loffay** 34:07 books.
**atoulme** 34:08 But yeah, thank you for, for the review on that.
It's, I think it's a good… it's a good discussion. I think it's, we're moving the lines inside OpenTelemetry, in terms of, like, not just what the operator should be doing, but, like, injector coming to help.
declarative config starting to play a bigger role. Your work on adopting declarative config is going to really move a lot of goodwill towards the operator project as a whole for instrumentation, and really also push more of the SDKs to pay attention to that. So, I think this is all very virtual cycle type stuff to kind of
Move things, you know, another turn of the crank towards the future we want.
So…
**Mikołaj Świątek** 34:50 There's actually something, like, vague related that I want to point out. I'm actually.
**atoulme** 34:55 Oh, good.
**Mikołaj Świątek** 34:55 to put this in Zoom chat, because we have, some… Questions about…
supporting the EVPF instrumentation in some generic way.
And…
This is… this is a little bit interesting, in the sense that it's different. Like, what they want to do is different than what you normally do, because their position is that this is incredibly inefficient to do as a sidecar, so what they want to do is they want to start a daemon set, and then instrument by making that daemon set look at the right.
Yeah.
On the node level.
And I told them that this is gonna be a fair amount of work to do, because we don't do anything like this right now, fundamentally. Instrumentations are just injections on webhook.
If you have opinions… and I wrote this in that issue. If you have opinions about this, or want to agree or disagree with me, because I was speaking for myself, you know.
**atoulme** 36:02 That's fair.
**Mikołaj Świątek** 36:02 out there. I don't really know much about how this… how the eBPF stuff works exactly, so I'm basically asking them to… to do a POC with Sidecar to actually show how it works.
**atoulme** 36:15 I agree with… so, sidecar's a bad idea. Are you aware that there's a HUM chart for this already?
**Mikołaj Świątek** 36:22 Vaguely, I am aware.
**atoulme** 36:25 Yeah, so the HAM chart, as far as I understand, is using a demand-set approach, and the reason to use a demand-set approach is because in the first place, when you run this type of eBPF-type library, you're going to need root privileges, so doing that on the sidecar, it's really… just really… no, not gonna happen. Also, getting…
specific processes sidecard sounds really, antithetical to what we're trying to achieve here, which is complete visibility of all traces inside the OS.
And if you're going to do that, you might as well do it for everybody at once on your box. So, they're doing that.
**Mikołaj Świątek** 37:01 I don't know how it works, which… exactly, which is why I'm… to begin with, I'm just asking, like.
show me a manifest of how this works, and how you, like… let's say you have this daemon set running, you know, how do you select what.
**atoulme** 37:17 Built.
**Mikołaj Świątek** 37:17 You're in… what you're… what you're looking at, for example.
**atoulme** 37:20 Okay, so they have some filters after the fact, after capture, but really what happens is that you pretty much you put a probe all the way down into the OS,
And anything that talks HTTP or TCP, you capture.
Right? And now you're saying, okay, PID X is this, PID Y is doing this, and then you start to correlate. That PID is actually inside that C group. That C group is connected to that docker. That Docker is inside that pod. And so you start to kind of aggregate all this information, all that metadata that you're getting from the information of what you can get.
And you say, okay, that pod has sent a request to that other pod. You don't know anything about the request. You barely know anything about, like, maybe the size of the message, or something like that, but you're able to intuit those two things to start.
That's good enough for most cases, right? And then you start to send, like, a span that says, you know, client span of
pod A talk to pod B, and then you send the service pad. Pod B receives something from pod A. And it's good enough for most use cases, and all of a sudden, you get a chart of… you get a graph of all the interactions of all the pods together talking to each other.
That is everything there is to know about this. This is how you get most of it. This is actually the second time that we're seeing this implementation. If you remember, this is an OpenTemmetry Network project under OpenTeometry, which is also doing the same thing, using
the same approach of probes in eBPF.
This new approach is more elegant, because instead of creating our own probes, we're using Silium, which is a relief in terms of maintenance, because otherwise you have to think about kernel versions, even what compiler used what version, because sometimes they're inline methods, and they're trying to capture a parameter inside of methods to understand what was being sent.
None of that happens here, and you're just doing this with Sirium, and you get a ton of value out of the gate, right? There's no profiling information, by the way. This is not the case yet. I don't think this is in scope, and it's very low level, and it's also very,
Very nice. One thing to note that's super important for here, for the operator, is that if they detect that you're running an OTLP exporter in your process, and they have ways to do that, right? They look for a port, they look for specific symbols in the code, or something like that, they know that you're already having this application instrumented.
And they know that the instrumentation, let's say, for a Java process, or Python, is going to be more precise and more versatile than whatever they can do with Selenium.
So, in that case, they explicitly stop monitoring that process.
Which makes it very complementary to your current instrumentation CRD. They don't compete, if that makes any sense.
**Benedikt Bongartz** 40:02 Sounds wild, especially when you have, then, custom Go versions with some compilers, and…
Then it's not detected correctly, and…
**atoulme** 40:13 You know, I believe they're marketing so far. We'll see if that works.
Because, but you're already.
**Benedikt Bongartz** 40:19 F?
**atoulme** 40:20 But the fact…
**Benedikt Bongartz** 40:21 As you said.
Go ahead, because you said you have to run. There is currently the initial draft pull request, or the pull request for the,
custom resource. And there was some discussion about what you mentioned also with the signals, should we have them, should we not have them, should we have a structure for it that we expose, and so on. And also, I think open territory related, we discussed about a few options, like.
Should…
I don't remember the options, but it was open telemetry options, like timeout, rebuffer size, and so on, if we want to expose this or not.
So what do you think about just removing most of it, just going with the defaults for now, so that we can get this CR, get everything in?
**atoulme** 41:09 Yeah.
**Benedikt Bongartz** 41:11 And then we can discuss when… what to add afterwards, and how to add it, and so on. So basically, in separate discussions, separate PRs, but then you can just…
Move forward, start playing with it a bit better.
**atoulme** 41:22 I was under the impression Gina had commented on it. She agrees with your comments to remove those options, and she was going to get there, but she did not. So, I'm pushing her a little bit around at this point, to think, hey, you really need to kind of get that done, and, you know, there are people who would love to help, so rather than having you being spearheading this, but also kind of sitting on it, can we… can we just ship whatever we have, and then
iterate. Like, we need to be able to kind of all work on this. So she understands that. She's working on, she's gonna pick up the feedback you have and remove those options, because they are, at this time, too much in the open discussion that we're not ready to have. I mentioned that multiple times with her. And,
we will be able to lend this PR.
I'm pretty impatient about it. I'd like it to be in people's hands, so we can get some real feedback, because having theoretical exercises about whether it's useful or not is not useful to me. I want people to give, you know, yell in my ears about what worked, what did not.
So, that's it.
**Benedikt Bongartz** 42:31 I think it's super powerful because of all the abstraction. I mean, on one hand, you cannot really treat much, but on the other hand, we can prepare things specifically for OpenShift, specifically for vanilla Kubernetes, and you can.
**atoulme** 42:42 Yep.
**Benedikt Bongartz** 42:43 It just works, hopefully, at some point.
**atoulme** 42:48 Yeah, I think I'm really trying to work with you guys on this type of vision of, like, you know, actually, the founding vision of this was, I'm looking at any OpenShift cluster to date comes with the Prometheus operator installed, and the reason people defer to Prometheus as the source of truth and the best approach to the OpenShift monitoring
It's just because it's there and requires no configuration.
That's an extremely attractive value prop, because no one needs to understand exactly what Prometheus did to get where it needed to be.
And I'm like, I want this, right? This is the use case, this is the lifecycle, this is the experience that people have come to expect from OpenShift.
And we come in, and we're like, you know what?
10 simple CRDs, and you'll be on your way. I'm like, oh my god. It's a discussion.
**Benedikt Bongartz** 43:36 The thing that I understood based on some conversations I had during a workshop was
A lot of people want to use the operator, they try to use the operator, they don't understand how the collector works.
**atoulme** 43:49 Yeah.
**Benedikt Bongartz** 43:49 they don't really care much, and that's what we discussed earlier with the braking changes. I can imagine that there are people reading just the operator breaking changes and don't care about the collector, because…
**atoulme** 43:59 You don't want to…
Yeah, right? So, and the more you customize, the deeper you get into a rabbit hole, and now you're sending queue parameter, change in the collector, and your whole operator upgrade failed.
Who do you yell at first? Like…
So, yeah, no, definitely, like, all of this, and, and,
I feel this is also a great way for the operator to be maximally useful, is to make choices for people, and to tell them.
You're going to love it, because by default, we're just installing some really, like, built-in capability. You don't need to think too much. If you want to peek under the hood, we'll give you access. You can define your CRD, you can have sampling ratio, you can do so much more. Look at all these options. You can have your own annotation system for that particular application you love and care about, right?
But, by default, here's what you're getting. And…
Easy, right? I want 5 minutes. Like, I've told my engineering team, every single customer is only going to work with Open Infinity at 4pm on a Friday. That's the only time they have.
How do you make them useful, given they have about an hour of exhausted time thinking about what they need to do for the weekend?
If you think about it this way, you might get some traction in the ecosystem. People do not want to spend 3 weeks thinking about OpenTeometry. That is not their job.
Okay, alright, Ivan, I'm running. See ya.
**Benedikt Bongartz** 45:28 Dylan, bye-bye.
I had another one, just to raise this,
I guess, after rebasing now, something is fading, but…
I changed all the configurations from command line flags that are currently exposed, or part of the
operator configuration to be also exposed as environment variables and change it in a bundle to just move this from A to B.
I was asking, do you have any objections about this?
The idea behind this, to summarize this shortly, is
On OpenShift, we install the operator using OLM, which makes it really tough afterwards to change the operator's configuration. So, for example, enabling a feature gate or something is not really
Possible?
And there is an option on the OpenShift installation, because it's… there is another custom resource, it's named subscription.
We can provide some configurations, like environment variables, and the idea is now the customer can go and just, for example, enable Go Auto Transmutation, or…
Enable a specific or disable a specific feature gate without needing to re-bundle the entire thing.
Yeah.
Since, Nikola, you are only here, I spoke already with Pavel, it's mainly a question for you. So, do you have any objections, or…
**Mikołaj Świątek** 46:51 Nice, baby shit.
**Benedikt Bongartz** 46:52 With the hand charts.
**Mikołaj Świątek** 46:54 I have… I… So…
I don't… if it's… if you're only affecting the,
the bundle for OLM with this, then… Sure.
I don't think anyone else Other than the OpenShift bits, specific bits themselves.
depend on this.
**PL Pavol Loffay** 47:28 We'll change as well the flex from the manifest that we generate.
Because it comes through the same source.
**Benedikt Bongartz** 47:38 Yes, so it will change it from flags to environment variables, but both is recognized. So technically, if the hand chart sets a flag, it still should remain to work.
**PL Pavol Loffay** 47:51 Interesting.
**Mikołaj Świątek** 47:52 President's border is the flaggiest…
**PL Pavol Loffay** 47:55 Is more important, right? The flag over.
**Benedikt Bongartz** 47:57 That's…
**PL Pavol Loffay** 47:58 with variable.
**Mikołaj Świątek** 48:00 It should. I would add a unit test for it, just to make sure that that's really the case. I'm pretty sure we have unit tests right now.
**Benedikt Bongartz** 48:07 Okay, here then.
**Mikołaj Świątek** 48:10 Yeah, this is… this seems fine to me.
And…
**Benedikt Bongartz** 48:14 Alright.
**Mikołaj Świątek** 48:15 I don't think there's any big difference. Assuming all of these actually, like, there's no bug in terms of, like, there's a misspelled environment variable somewhere in the code, and we just never know this because nobody ever actually uses it. That's, like, a possibility.
And I don't think there's actually a test for this manifest.
In the sense that I'm not sure if anywhere there's, like, a place where we take that manifest.
Install it into a cluster, at least in the operator repository, and verify that, like, it actually starts, or something.
I'm not sure that…
**PL Pavol Loffay** 49:01 We do it as part of the end-to-end tests, we generate the manifest, we install it to the kind cluster.
**Mikołaj Świątek** 49:07 I'm… I'm pretty sure we use the cus… we use Customize.
I don't think we generate this for this specifically, this full manifest. Or I guess you're changing the customized ones as well, right? So…
**PL Pavol Loffay** 49:20 Yeah, he's changing the customize.
**Mikołaj Świątek** 49:23 In that case, it's probably fine.
**Benedikt Bongartz** 49:25 Okay. One other thing, just probably because you're here, so with changing, for example, the lock level, this is used… it's not part of the configuration, of the operator configuration.
So this is coming from the CRI, and the CRI library that we are currently using, I don't remember, was it Copra or something?
As far as I… I just looked it up for a few seconds, it seems it doesn't support environment variables.
So, which means, if we don't set this as a flag currently, it's not possible, so one nice way to make this work also with environment variables is either at some implementation to make this work with environment variables too.
Or just change the library, and I was thinking…
**PL Pavol Loffay** 50:14 it was optional comment, you can ignore it. I was more…
Because the environment variables that you put in the changelog those… kind of… that configuration
It's not something that end user would do, because you were changing, like, the metrics, or something that…
even though you can change it, most users don't change it, and even if they do change it, they would need to change other stuff, other all Kubernetes objects. So I was saying, like, hey, maybe you can instead
Look at something what most people want to configure, which is
maybe the log level, but I think…
Now you got it right at the feature gates, is it something that people want to.
**Benedikt Bongartz** 51:01 Yeah, but I misunderstood.
**PL Pavol Loffay** 51:02 That's your patient.
**Benedikt Bongartz** 51:04 But I misunderstood you, because I didn't put this into the changelog, I just sent… yeah, no, it works, also with feature gates.
I didn't understand you would like to see this in change enough, but I can put it there. So I put the feature gates and something more common there.
**PL Pavol Loffay** 51:18 In a change lock. Yeah.
**Benedikt Bongartz** 51:23 Yeah.
**PL Pavol Loffay** 51:23 Pizza.
**Benedikt Bongartz** 51:24 image.
**PL Pavol Loffay** 51:24 What a good success.
**Benedikt Bongartz** 51:27 is what popped up when I… Rebased.
Yeah, I will fix it, and then just ping you again.
**Mikołaj Świątek** 51:50 Okay, I didn't say I have…
**PL Pavol Loffay** 51:51 Like, are you coming?
**Mikołaj Świątek** 51:52 Yeah. Are you coming to Amsterdam?
I don't know for sure, but probability is, like, very high.
Are you?
**PL Pavol Loffay** 52:03 We should be there with Ben as well.
**Mikołaj Świątek** 52:06 Cool.
**Benedikt Bongartz** 52:08 So we can go for pizza.
Typical…
**Mikołaj Świątek** 52:11 Yeah, specifically pizza? I, I've… And I remember, I remember there's, like, this nice place selling Lebanese food?
Close to the, close to the old city.
That I really liked last time.
I see you're not happy, you really want the pizza.
Why do you want pizza in Amsterdam?
**Benedikt Bongartz** 52:34 I think Paris was pizza, right? Where we got pizza outside.
**Mikołaj Świątek** 52:39 In Paris, I was… I actually ate, crepees.
For dinner, at least twice.
**Benedikt Bongartz** 52:48 Yeah, I think for lunch, we went for a pizza. And, no, in Amsterdam, we got.
**Mikołaj Świątek** 52:52 No, you know, in Paris, we did go for a pizza. That was the… that was when the well-dressed gentleman recognized Christos Marco as a speaker. I still remember that, because it was so nice.
Whoa, Kubernetes speaker in the flash.
**Benedikt Bongartz** 53:13 Yeah, so…
**Mikołaj Świątek** 53:14 Hmm…
**Benedikt Bongartz** 53:15 Yeah, maybe we can organize something to go for lunch or dinner, whatever.
**Mikołaj Świątek** 53:21 It's likely that there's gonna be an auto.
Dinner of some sort, as well.
**Benedikt Bongartz** 53:27 There was one in London.
But it was in London, too. Usually it was organized by a jury, right?
**Mikołaj Świątek** 53:37 Hmm… It was organized by Jurassi in Paris.
In London, I… I'm not sure. I think in London, it was, like…
I think it was actually Elastic doing it in London, and he said it was maybe as a… as an employee. I know that we were…
**Benedikt Bongartz** 53:59 Actually, you have been the organizer and you just forgot.
**Mikołaj Świątek** 54:02 I think it was co… kind of co-sponsored by… by Elastic and Grafana.
Sorry, by, yeah, by Elastic and Grafana Labs, but, I don't know who actually, like, took point on it at the time. And I know that there's gonna be one again, but, but it, like, it's… it's quite likely. If it's… if there's not, we can also go wherever on our own, too.
It's weird, because the freaking, like, KoopCon dinner, like, what you do on dinner during KoopCon is, like, a very contested space, suddenly.
Because I go there, I'm definitely gonna have some kind of Elastic-specific meetup on one of the days. There's gonna be an auto dinner, and then, you know, you don't have many days left after that.
It's not that easy. And of course, KoopCon has its own, like, whatever, beer crawl or whatnot, which was really bad in London.
**PL Pavol Loffay** 55:05 Yeah, the food at KubeCon is terrible, usually.
I don't understand how they can actually do that to people sometimes. I… I think the…
**Mikołaj Świątek** 55:17 I think in Amsterdam previously.
the food was actually alright, or, like, they actually had, like, stalls with hot… various, like, hot, kind of, fast food. Yeah, I mean, especially the sandwiches for lunch, those are…
**PL Pavol Loffay** 55:34 Notes.
greatest…
**Mikołaj Świątek** 55:36 No, no, they are.
**Benedikt Bongartz** 55:37 But they shouldn't…
On the observability day, they had really nice… so on the co-located event day, they had really nice snacks, and this was really nice from the food. So I was really happy. The next day, I went to the conference, and then you get all this dry bread, and…
**Mikołaj Świątek** 55:57 I have learned to pick whatever… I've learned to pick the vegetarian option.
Because I don't… I don't trust the… I don't trust what they do with the meat.
Anyway, I'll probably… I'll very likely be there. I don't have confirmation yet, but… but it's like, unless something weird happens, it's… I'm gonna be there.
Okay. Awesome.
**PL Pavol Loffay** 56:25 To know if you are there to organize the hotel, right?
**Mikołaj Świątek** 56:29 I'm not organizing anything unless somebody orders me to, okay? And, like…
It's… it's… I get tired enough just attending the conference and traveling.
a little flies.
You want me to, like, go and, herd, like, 15 people to dinner? No way.
Anyway, I'm, I'm… I'm off. I'm, like, really tired today. I'm kind of looking forward to…
Signing off.
See you guys later.
**PL Pavol Loffay** 57:05 Speaking of goo, bye.
