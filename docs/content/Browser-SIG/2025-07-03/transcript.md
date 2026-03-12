SIG: Browser SIG
Date: 2025-07-03
Duration: 38 minutes
============================================================

## Zoom Recording Transcript

**Ted Young** 01:07 Hello! Hello!
**Jared Freeze (embrace)** 01:11 Hey!
**Martin Kuba** 01:12 Good morning!
**Ted Young** 01:14 We finally did it.
We started the browser. Sig.
People are new. I'm just gonna post a link to the agenda.
Alright.
You can find the agenda from the calendar. Invite as well as well as the community repo. Recommend. People add their names to the attendee list.
If you have any items you want to talk about. Please add them to the agenda, including any Prs you'd like viewed.
And barring anything else I'd like to use this kickoff meeting to just start to get our different work streams organized.
the goal would be to get things organized to the point that people can start picking off issues and items and assigning them to themselves. And.
you know, starting to get productive to that point, does anyone consider themselves to be like a Github projects wizard like they feel like they're they're fairly familiar with github projects.
No one is that's fine. We're trying in general and open telemetry right now, trying to learn how to use projects. A lot better projects used to suck because they they just didn't have any features.
But they've added quite a number of features recently so trying to figure out what the most optimal way might be to to put everything into a Github project and then show it to people.
**Jared Freeze (embrace)** 03:55 Last time I used it it was in the didn't work that well phase so.
**Ted Young** 04:00 Yeah.
**Daniel Dyla (Dynatrace)** 04:01 Yesterday.
**Jared Freeze (embrace)** 04:06 Exactly.
**Ted Young** 04:20 Yeah.
Okie Dokie.
alright, let's kick things off. So only thing I see on the agenda is from Jared. Asking about new repo.
I think we need to figure out what what we need a new repo for for us to to make one. It's easy to make one.
But do we just want something to put issues and stuff in?
What are we gonna put there versus the Js repo?
**Daniel Dyla (Dynatrace)** 05:19 Personally, I'd rather do stuff in the Js repo, if you know.
if for no other reason, then the work is pretty related. And it's already there, and it'll be easier for.
**Ted Young** 05:36 Me to keep track of your things.
**Daniel Dyla (Dynatrace)** 05:40 But if we want our own repo, that's fine as well.
**Martin Kuba** 05:50 Yeah, I mean the only reason that I that I thought would be good to have a separate repo or a couple of reasons. I guess one is this that you said have issues and Prs or issues, mostly like in a separate specific place. It's easy for people to see like where to find things for browser. Right now it's kind of not easy.
And second is just have more control over like releases.
the android sig that that's their model. They have a separate repo built on top of the Java SDK. But maybe we'll just don't need it right away. But that's.
**Daniel Dyla (Dynatrace)** 06:34 Yeah, certainly, when it comes time to actually like write instrumentations and stuff, they need to be released from somewhere and and regularly maintained. And whatnot.
There are some instrumentations in the core. Js repo. Most of them are in the contribute Js repo, including, I think, right now, all of the browser instrumentations. Maybe Trent can correct me if that's wrong.
**Martin Kuba** 07:02 Not all of them.
**Daniel Dyla (Dynatrace)** 07:02 The so.
**Trent Mick** 07:05 Then counter example, but otherwise, yeah.
**Daniel Dyla (Dynatrace)** 07:09 Yeah. The contribut tends to be a little bit more wild, Westy.
Then the core repo, and it tends to be more difficult to get reviews over there, and it's less clear. You know, we have people that contribute stuff and then walk away from it all the time. It can be frustrating to work in. I understand.
but the core repo I think we do a better job with. I hope we do. I feel like we do.
But yeah, if we if we feel like the the needs are different enough to have a separate repo, I'm not against it.
**Ted Young** 07:47 The the 2 things that come to mind is like maintainer management.
right? If we end up with 2 piles of stuff that have mostly different maintainers.
And then the other is just like from a practical aspect of like build tools.
Does the the build pipeline for the browser become like, like, very different from the build pipeline for node. And does it somehow help everyone's brain to have 2 separate repos for that reason? I don't know if that's true or not, that's the other thing I can think of.
**Jared Freeze (embrace)** 08:30 I think it partly would come down to like browser targets and things like that, right? Because not everyone's gonna import and have their own builds like, I don't know if there's an idea to provide something on the Cdn. I mean, if that's the case, you can't just run with 2022. Necessarily, I don't know if that's something. I I saw that the 2 dot o is it committed to es 2022 so I I don't know something to think about. If there's actually something provide like a package provided for the browser directly, instead of just the library.
**Ted Young** 09:08 Great.
**Daniel Dyla (Dynatrace)** 09:09 You're talking about the 2 dot O. SDK, I assume? Right.
**Jared Freeze (embrace)** 09:13 Yes, yeah. So I saw that they're gonna yeah. The floor now is, yes, 2022.
**Ted Young** 09:23 Great.
Okay? So my suggestion is, let's let's wait until we feel like we need a browser and try working out of the Js repo for the time being, you know. But let's let's be quick to to make one.
**Daniel Dyla (Dynatrace)** 09:40 We can also add, people with triage permissions and such. Yeah and right and and whatever as needed, in order to to make it work a little better.
**Ted Young** 09:53 Yeah.
Yeah. Triage approver, etcetera.
I feel like trusting people to be on good behavior and not misuse her authority.
We can give that shot.
Okay.
On a related question, there is the Js sandbox web. Js, whatever it's called repo.
Is there anything in there that that we want to keep. That's relevant going forward. Or was that just an experiment? And we should archive it to avoid confusion? Now that we're working on new stuff.
**Daniel Dyla (Dynatrace)** 10:36 I think there hasn't been a lot going on over there for a while. It looks like 4 or 5 months ago there were a couple of changes.
I wasn't aware that it was even still alive. To be honest.
**Martin Kuba** 10:51 Yeah, it's not. It's not being actively used. I don't think. There is a branch that has some prototype on it which I don't recall exactly everything that it has in it. Maybe before we delete it, I would like to take a look, but I don't think we'll be, as far as I know, using it.
**Daniel Dyla (Dynatrace)** 11:08 Yeah, there's 1, 2, 3, 4, 5, 6, 7 commits in 2025 and 0 in 2024.
**Martin Kuba** 11:16 Yeah.
**Daniel Dyla (Dynatrace)** 11:16 So.
**Ted Young** 11:17 But it's like we can move it just like the open. The there's like a Js Api repo. That's archive, right like when you archive something.
**Daniel Dyla (Dynatrace)** 11:26 Still exists.
**Ted Young** 11:27 Did.
**Daniel Dyla (Dynatrace)** 11:28 Yeah.
**Ted Young** 11:29 So maybe that's what we should do is like a community. Follow up. I can make an issue just to get that moved to public archive. I just wanted to flag it if people felt like they had work. I think it was mostly nev's playground, so I think it's probably fine to just go ahead and archive it.
Okay, And then, David, you had some Simcom Prs.
**David Luna Bistuer** 12:00 Yeah, just a heads up. So compliance limitations. And I think that also one of them is already closed as well. So maybe it will be good to be. I cannot reopen it. So I had a look, and well, just a kind reminder of maybe we can push this forward and have some other questions would be, would be good if we start doing something, and then start previewing implementations and and instrumentations to have at least even if it's in development status. But to have something in the simcom.
**Ted Young** 12:37 Yeah, yeah, this this dovetails with. Getting our backlog organized. I think the 1st one clear path of work that we have are semantic conventions right? And we can divvy those up into, you know, browser fundamentals and like library. You know, conventions or things that don't do with Browser. I think everything we find so far is like a browser.
You know.
Runtime convention. We could probably just stick to that as our work stream for the time being. But it would be good to get that into some kind of like coherent work stream like so one so that we understand like completeness. That's like a question I have is like, how do we figure out what complete this means for simcom and instrumentation for the browser? As far as like what we're actually trying to achieve.
It would be nice to have some way of just being like slightly scientific. And we can say like this list, we came up with is the right set of things because of something we're pointing at But regardless of that, we should come up with a list of stuff that's, you know.
already added stuff that's in flight. And then stuff that's to do's.
And I can put them into a project board or create issues for them, or something like that, so that it becomes easier for people to start assigning them to themselves and picking them up and getting them done that seems like a work stream. We did divide things in kind of into like phase one and phase 2. But it seems like that's a work stream. That's like pretty independent from the other work we're doing. So.
you know, in the names of moving faster by moving in parallel, I think we can continue to work on that while we're also thinking about things like like the Api packages and stuff like that.
Does that resonate with people? Do people feel like we can keep working on browser semantic conventions, or do people feel like there's some other fundamental work that we should address 1st and like, put a pause on that stuff until we get it done cool.
I'll take silence as agreement that there's no reason why we can't can't keep going on that as long as there's people interested in working on it.
So the question is just like, what's the best way to to organize that. So it's like easy for people to find So maybe for starters. I see, Martin, you put work in progress just into the Google Doc.
Let's maybe just like add another tab under here for You know.
some common needed people want to start populating that list in the doc. That would be great. I can. Then I'm conscious we're trying to do 30 min meetings instead of our long meetings. So you know, offline. After this meeting I can take a pass.
I kind of like putting this stuff into a project board, but I don't think everyone needs to like. Watch me do that and then I'll post in our slack channel with like my 1st stab at that project board in a way for assigning issues, and people can critique that and be like this is useful for me, or like this is confusing.
Does anyone have an idea? For where we could get a kind of master list of like, say, all the browser events that we want to.
We want to have semantic conventions for.
**Martin Kuba** 16:42 Yeah, I mean. So I think we have. We have in in the original client Sig board.
I think we have a bunch of issues there.
So I think all the all the events that we agreed on in the past. They have issues there.
**Ted Young** 16:59 Yeah.
another kind of like related thought.
And this comes up. I've noticed also, when we are trying to make semantic conventions for these events is like, which attributes do we want? And how do we want them represented? And the answer to those questions comes down to like, Well, what do we want to do with this data?
So I also think that something that would be helpful for this group early on to get together is kind of like a model, for, like browser observability, not everything. Everyone could do right. There's all kinds of like advanced features and workflows when it comes to like rum products that are out there. But we're not. We're not trying to do all of that all at once, right? Like we have some subset of browser observability that we think is useful out of the box that can be accomplished without doing things like complete dom replay kind of stuff that you see in some of the more advanced things, but I think it would probably be helpful to identify like what what it is we're trying to like. Offer people not all the different ways someone could use the data. People can be creative. But we should have like a way that we expect this data to get used so that we have some kind of like guiding star when it comes to making the rest of our decisions.
And also something to kind of like present and critique.
So because presumably it seems like this browser stuff. In particular, you're making trade-offs between like efficiency and data collection and stuff like that in a way that's like a little bit more hard edged than you're having to do in other environments to the resource constraints. So having some kind of observability model that we're in agreement on will probably help us get unblocked when we get blocked on on some of these issues.
Anyways, that's something I can start. But again it it would be kind of helpful to maybe point to something that's already out there.
So food for thought. If anyone knows of like anything you've seen, even like a good blog post that's like or picking an existing implementation that we feel is like, Hey, that thing over there is kind of like right size for what we're trying to do, Pharaoh. I mean, I work at Grafana labs so familiar with Pharaoh, but it's like an example to me, because it's like a relatively new thing. And it it does seem to do like a good job at like basic stuff. But it's also new. So it doesn't have a lot of like crazy features, whereas if you look at what maybe like dynatrace or or sentry, or something like that, you're talking about things that have been around for like a really long time.
**Martin Kuba** 20:01 And do like 18 million things.
**Ted Young** 20:05 But it could also be. We're looking at those things, and we're like picking off like we we want to look at like the kind of like performance analysis that these tools do?
whatever you does that does any of that make sense to people as far as like picking a target for us to aim for.
**Daniel Dyla (Dynatrace)** 20:22 Yeah, as far as I know, there is no like full like open source like, you know.
I don't know what I would call Prometheus for rum like, well used in the industry, like standard open source implementation. I don't think there really is one. Unfortunately.
**Ted Young** 20:42 Yeah, you know.
But I think I think something like that like, if we're saying we're we're gonna be building sessions. Right? People are going to get a resource called a session. And in that session they're gonna get a bunch of events right? They're gonna get a bunch of events that are associated with the browser and associated with resources like session, but also user Id and other things. And then they're gonna be able to create like they're going to be able to look at those as logs, and they're going to be able to create dashboards out of them.
And those are like the most basic things you could do.
and you can create traces out of them for the parts they're tracing. And those are things you could do with kind of like any generic observability product. Right? You don't need a rum product to look at this data.
but is that like? Is that all we're trying to give people. Is there something coherent like if we're saying like.
Take open telemetry, browser, and install it? And now, like, here's like our playbook, for, like how you should observe the browser.
It feels like to some degree we should be writing at least a bit of that playbook.
so that we have an understanding of what it is. We're trying to give people right now rather than just give people like a big pile of stuff and say, like you, you figure out how this might be useful.
I don't wanna overclock on that, but it just seems like like something useful to to be developing.
**Jared Freeze (embrace)** 22:26 I mean. My my 1st thought was resource timing, which I see on the list already. So you know, Major, assets that are in your way, you know. It'd be nice to just very quickly be able to see. Hey? Ads are destroying my page, whatever you know, something like that.
**Daniel Dyla (Dynatrace)** 22:44 Yeah, basically, whatever you see in the inspector.
**Martin Kuba** 22:53 I mean, there's but there's, I think we know some of some things like page views. Also, like customers want to know, like how many users are coming to their websites, and where they're coming from.
Errors. Obviously,
**Ted Young** 23:08 Cool. So maybe that's like a good guiding star is to maybe come up with like a list of problems like these are like common problems people want to solve. These are the things people are installing, bothering to absolve observability for their browser stuff because they're looking at these kinds of problems.
and to have kind of like a list of those and an understanding of how you could use open telemetry to look at those things in some kind of generic back end right like we don't want to come up with a model right now, for like, here's like some rum product we expect everybody to build. But it's more like, if you were just like taking this browser data and shoving it into some generic set of like stuff like you should be able to create dashboards and alerts to to look at these things, and you should be able to look at this stuff as logs and traces, and use all these kind of like generic tools and solve some subset of like important things you would want to solve.
In the browser. And that's probably like a good starting point for for what we want to do. And then, later on, down the line, we can think about some of the more advanced things that that people do with rum, but just as far as getting our basic data model together of like which events we should be recording which attributes should be on those events, you know, having this target of like.
how you would actually try to use this thing probably will be helpful for guiding that.
Okay?
Dan, you have food for thought on Api changes on here. I'm going to become.
**Daniel Dyla (Dynatrace)** 24:47 Yeah.
**Ted Young** 24:47 Time. So this will be our last item for this meeting.
**Daniel Dyla (Dynatrace)** 24:50 Yeah, I mean, this isn't really a 5 min topic the the other Js Maintainers are here. They're already familiar with it. Martin has already seen it. I don't know how closely you looked at it.
One of the things I noticed in the project proposal for this Sig was potentially a fork of the Api I'm full cards on the table right now. I am a hundred percent against that. At the moment.
It would take a lot of convincing.
not just because I wrote most of the Api. There is some like, it's my baby energy that I just you know you can't get rid of, but also the user experience of like an end user having to decide which Api to use, in which case and they would have to interoperate together like, if I write a MoD like some some Npm module that is expected to work in both the browser and the and in node, which Api do I target?
I I think it's a lot more headache than I. I honestly. And I know, Ted, you're you've been quite against this for a long time, but I would much rather go to a 2 dot o of the SDK that works in both cases.
**Ted Young** 26:12 I'm not against the 2.0 of the SDK hell.
**Daniel Dyla (Dynatrace)** 26:14 Oh, Api! I'm sorry. Api.
**Ted Young** 26:16 Hmm
**Daniel Dyla (Dynatrace)** 26:18 Shadow of the Api, which I know is is tentous.
Certainly there would need to be a bridge layer for some period of time, potentially forever.
That users of the old Api would be able to opt into. But users of the new Api would not be obligated to use.
I?
Yeah. So that that's context for this, I had already started working on this poc, as like.
what would I do if I could start from scratch again.
There were a lot of change. There's a lot of problems in the existing Api.
Specifically, around browser. I bundle size is the really really big one. It's massive.
If you click on. If you look at the read me here and I I can share my screen. If if that's easier.
There is a section in here about the bundle size the old Api just the Api without the SDK using the same webpack configuration that you can find in here.
Bundled and minified is 23 K.
It's massive. It's huge.
This Api is under 4, and that's with nothing tree shaken out. So if you only use events, you could tree, shake out a lot more.
It double emits Esm and common. Js, so if you're using. Esm, your tree shaking is more effective.
It drastically reduces a lot of the sort of mechanisms that we had used for backwards compatibility checking and things like that, because in Js using Npm, it's very easy to have many versions of the same module installed on your system and having them all kind of interact with each other can be frustrating.
It does this by going to a like event. Emitter based model.
That I called a channel. This is loosely based on the idea of diagnostics channels from Nodejs.
But it's essentially an event emitter. It calls things synchronously.
It's a little bit weird because it's optimized for extreme performance, especially in the case that nothing is listening to it. So it starts as a no OP.
And modified itself when you originally subscribe to it. I can go deeper into this on it. At another time, if people are interested.
**Ted Young** 29:20 I mean I.
**Daniel Dyla (Dynatrace)** 29:21 But what that means is that the Api emits an event. If the SDK is listening to it great, and if it's not, there's no problem. So when you add new features to the Api, it just emits new events.
and if you haven't updated your SDK yet, you just don't get them.
It. It removes the requirement we previously had, which is, when you updated your Api, you had to update your SDK, or a wooden compile and it makes the backwards compatibility story a lot easier. That was the main motivation around that I know we're out of time now.
I would encourage people to look through this and consider what I've done here. I do not at all. You know I put this. This is proof of concept, only it should not be considered roadmap in any way.
But personally, I would much, much rather go to a 2 dot o api that works better for browser and web than to fork. I think forking is I I just think it's a mistake. I I'm willing to entertain arguments if other people disagree.
But that's my starting point.
**Ted Young** 30:43 Yeah, just to be clear, I'm not. I'm not against this at all. I think it's great. And I think this dovetails with, like the other work stream that we have to kick off, which is like Api review.
I think the main reason why forking comes up is, I believe there are places. It's mostly the tracing package. But there were places where the capabilities of Nodejs and the capabilities of the browser, I think, in particular, around context, propagation diverge and trying to like paper over that in a generic way, ends up being really like heavyweight in the browser environment, or like not optimal. And think that was like kind of the crux of it.
We're not gonna load the metrics, Api, because we don't need it, so we don't care, and I can't see how the event Api would diverge between the 2 things right like the event. Api seems like very simple, so I don't see why we would ever need, somehow, some special browser event. Api. So it's really just like the tracing stuff and context, where?
But I don't know what the answer is, if the answer is like you solved it, and it works in both places, or like modern browsers and Nodejs. Now finally agree on something.
That's great.
But that's my understanding of like, where potentially you would want to stop pretending you had some feature in the browser. That you don't have. If that was like actually making everything worse performance and load time and everything for the browser.
So you'd want a version of the Api that didn't pretend, like you had access to something and force you to do it like a cranky way that you would want to do it in Nodejs and then for people who run in both environments, they would just need to pick the browser one and these 2 Apis would be have to be able to interoperate with each other.
Which is also the case with this. By the way, I would not call this personally my approach. And again, I don't. Maybe in Js, there's a way to do this, but it wouldn't be to have a 2.0 Api. This would be another Api, another 1.0 Api, that we're adding right? Just in terms of like dependency management.
Nonsense. Right. You want people to be able to some packages to run the old one, and some packages to run the new one, and all that, to be able to be compiled and like them to interact with each other. I'm sure you've thought about this stuff. But.
**Daniel Dyla (Dynatrace)** 33:17 Yeah, that's that's still possible. If you go to 2 dot. O.
**Ted Young** 33:21 In some languages it is not.
**Daniel Dyla (Dynatrace)** 33:24 In. Js. It is, and I think it's a much more clear signal that, like this is the path moving forward for both browser and node, and that like, if if you add a new Api, and you have 2 Apis that are both one, you then are constantly fielding questions of which one should I use?
If you have the same package that has a version one and a version 2, it's pretty clear no one's gonna ask you, should I use the old one when they're starting a Greenfield project?
And it's a clear expectation that, like the old one, will not be maintained after some period of time, which I would also expect.
**Ted Young** 34:03 I think that's great. If that's possible, it's just that in some, in some languages, right? You can't have both a 1.0 and a 2.0, because you're gonna have some like the SDK, for example, you'll have these packages that would need to interact with both. So they would need to import both. And in some languages that's just like, not a thing. Or it's like.
it's like you get it. It's like hell starts to happen for people. It becomes very difficult to manage your dependencies. So. But I, my feeling is just to get broad right before we get off. The call is like, I feel like open telemetry is hitting kind of like a 2.0 in the sense of like. We have all these implementations in all these languages we've all been following a generic spec to like. Make sure we don't screw that up in a bunch of, you know, potholes that we know about. But now we're like mature where we have these mature communities in each language. And I'm sure for each language like Javascript, that community can now look at what we've been doing for years and be like, I see all these different ways. I could improve this if I started to get very like language specific about this thing and moved away from like a cross browser. Specification.
So I'm actually in support of that. if it's done.
you know, with like a lot of like care and intention.
And if this also like solves our browser problem, then I think that's that's fabulous. So great it would be great to learn more about this offline, since we're out of time.
Is there like a presentation that we could watch if you like pitched this somewhere.
**Daniel Dyla (Dynatrace)** 35:47 I can. I can make one, if you'd like, for the next meeting. But I have not recorded anything. There's I haven't really shown this off very much to anyone other than the Js. Sing. For a short period of time.
**Ted Young** 36:02 I think I think that would be helpful.
to have a a recorded pitch, or like a written one, or some some way for people to understand like cause. It is like a pretty big deal. And it's not just Js people right like the Tc. Like other people, are. Probably once they catch wind of it, they're gonna be like.
what are you doing over there? So.
**Daniel Dyla (Dynatrace)** 36:24 Yeah, that's why I put it on my personal github and put the note there that like this is not to be taken as an opinion of a maintainer. This is an opinion of a person.
**Ted Young** 36:34 Yeah.
Well, this is certainly good timing, though, if you're saying like, we can solve a bunch of problems for node. But it also solves all the problems that are blocking browser adoption of the Api. Right like that alone is great motivation for doing this. If we're saying, like, we have to come up with a new api anyways, because the current one is unfeasible for the browser just coming up with one that works everywhere.
**Daniel Dyla (Dynatrace)** 37:02 Yeah.
**Ted Young** 37:03 Agree that that is better than like having 2 flavors.
**Daniel Dyla (Dynatrace)** 37:08 And I've already been working on this. It's it's timing was a little bit fortuitous, because I had just kind of started actually prototyping some of these ideas that we've talked about for a long time. I mean, I don't know when the when I 1st brought these up, but you know I. I probably 1st talked to Mark about this idea of an event based Js. Browser, Api. 2 years ago.
**Ted Young** 37:30 There's, I mean, when you say event based, I'm like, do do we still have spans like what's going on here? But I can. We're out of time, so I can. I can look at it there. But it also seems like I know the node at least some people in Node core. If, like, pop their head up and be like open telemetry like Node should directly work with hotel in some way, and that's been kind of like.
you know, gone has been as much of a bike shed as one would imagine. Something like that would be. But it seems like this would dovetail with that conversation as well, giving people an opportunity to have a place where they could have their say rather than just take on something whole. Hog.
Okay?
Yeah, give us give us a pitch.
This seems really important.
And Ken, I saw you asked the question. Want to move that to slack, and then we'll continue the conversation there.
**Ken Rimple** 38:27 Yeah, we'll do.
I'm sorry. The short. The answer is, yes, okay.
**Ted Young** 38:32 Yeah.
Yeah. An underlying mechanism makes sense.
All right. This is productive. 1st meeting. I'm going to follow it up by taking a 1st pass at this project board, and I'll I'll ping you all on slack when that's done.
**Daniel Dyla (Dynatrace)** 38:46 Sounds good.
**Trent Mick** 38:47 Thanks.
**David Luna Bistuer** 38:49 Right.
