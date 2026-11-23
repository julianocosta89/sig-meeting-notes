SIG: OpenTelemetry PHP SIG
Date: 2026-11-18
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Paweł** 02:33 Hey, Brett.
**Brett McBride** 02:34 Hey, Pawel, how are you?
**Paweł** 02:37 I'm okay, thank you.
Sorry for being late.
**Brett McBride** 02:40 That's alright.
I can see that a couple of people have got the agenda open, so I think maybe there's another person coming.
Wow.
**Paweł** 02:51 Yeah.
**Brett McBride** 02:52 is… It's like, what is the one for the wrong thing that we actually learned? And I'm like, is it a lot of nerds!
**Paweł** 03:05 No, it's so dark still.
Outside, yeah.
**Brett McBride** 03:10 Sorry to hear that. Oh, God, Chris.
**Chris Lightfoot-Wild** 03:14 Welcome.
**Brett McBride** 03:14 Holy fuck.
**Paweł** 03:15 It's ever dark.
**Chris Lightfoot-Wild** 03:19 I could just please…
**Paweł** 03:20 Where are you? Are you in the cave?
**Chris Lightfoot-Wild** 03:23 I'm in the office, which is above the garage, so there's no light on in here.
I can put a light on, one second. I'll splash out.
Hello.
**Brett McBride** 03:46 Much better.
**Chris Lightfoot-Wild** 03:47 Hello, what?
How you doing?
**Brett McBride** 03:52 I'm well. Welcome back, hope you had a nice break.
**Chris Lightfoot-Wild** 03:56 Yeah, thanks very much, yeah. Excellent. Loads of steps.
**Brett McBride** 03:59 Oh, yes.
You probably feel much better for that, too.
**Chris Lightfoot-Wild** 04:04 Yeah, nice to have a restaurant, huh?
**Brett McBride** 04:07 Yeah.
**Chris Lightfoot-Wild** 04:07 We did some, like, quick maths, and it was, like, a total estimate based on, like, what a smartphone said would cover. So that's 70-odd miles.
Which, you know, like, is not loads, I suppose, if you're sitting out to walk, but just walking around slowly.
Poil it?
**Brett McBride** 04:24 That's a… that's a lot.
**Chris Lightfoot-Wild** 04:27 Hmm. We were like, oh, that's like 3 marathons, pretty much, right?
**Brett McBride** 04:31 It is, yeah.
**Chris Lightfoot-Wild** 04:33 There's no way we could run, so…
**Brett McBride** 04:38 Yes.
Alright, well, I've got the… I've got the agenda up and open, so I'm happy to… to drive today.
Sorry, let me just copy some… Attendees.
So I wasn't sure if, Our new… our new maintainer, Tobias, might show up today. He said he was a maybe, but he'd have to ask his boss to change a meeting, so… Yes, but, you know, we also have some… some flexibility about the meeting time. I take it you prefer slightly later than, oh no, we bump into your Start of workday, if we go much… Light-to-reakers.
**Chris Lightfoot-Wild** 05:38 Yeah, but that's, you know, I don't have to be around either. I'm flexy.
**Brett McBride** 05:43 Yeah. Yes. Alright, noted.
Alright, well, let me fly through the… through the agenda, or what I had, which mostly is carried over from… from last week. So, I tagged new versions of everything.
But that was probably… A week or so ago.
And I know that Pawel wants, some more things, I think particularly the SDK, but I'll just re-tag everything.
just to jump ahead, I've been doing a lot of work in DevTools to automate the release process as much as possible. We've got bots set up that can create pull requests.
Etc, so… I've got… I've just got a couple of, sort of code review fixes to apply, from… from Pawel's suggestions, and I might get that done in the next day or so. So I think we're very close to… A release being a, like, a one… one maintainer job.
I.e, the ticker box, approvable pull request, and… You know, everything just happens.
I hope. So, I'll find out. But, in terms of how getting a release out, I'm happy to just do a manual one.
And get everything out. It was… it was… it's mostly automated anyway, it's just me typing commands instead of clicking buttons, which I'm quite happy to do, so I might try and get that out. Like, today.
I thought so.
**Paweł** 07:24 Thank you very much.
**Brett McBride** 07:25 Tooth?
The other notable things that happened were we had a, a security vulnerability report, which you might have, might have seen already, but it was really interesting for me, having not done One of these before, just to go through the… go through the process, and, like, the secrecy of it all, and… Yes.
Yeah, so, we… OpenTelemetry has a, like, a security roster, so I had someone from, sort of, the core team there to basically hold my hand and clear roadblocks, as… as needed, so I was able to get things done really quickly.
Which was… which was good.
And the only other notable thing for me, Chris, because I hadn't forgotten about our… we need to add more, maintainers.
or adjust the maintainers. Sorry about this background noise.
Which is, well, two things. I did a check and discovered that Bob was the only maintainer on a couple of our packages in Packages, so I managed to get ahold of him and he added me.
And I had a PR, merged against Packages itself, so we've got the APIs now to… added maintainers. So, I will be able to use that to add the OpenTelemetry PHP user to everything, and Chris, maybe you can run with that to have it Add maybe a second maintainer.
Into packages, as we create an update.
Things.
Yeah.
**Chris Lightfoot-Wild** 09:20 I'm…
**Brett McBride** 09:20 to the… to the API, but it's in the API docs now.
So…
**Chris Lightfoot-Wild** 09:27 Excellent.
**Brett McBride** 09:28 Yeah, that's it. That's it for me. Chris, I see you've got… I've seen… I've seen one issue for this that I recall.
about SEMCONF 145.
**Chris Lightfoot-Wild** 09:44 Well, someone had already opened a PR against it with some apparent fixes in, so I just wanted to just highlight, because I think we'd had this conversation in the past, I don't know if it was when you were around, or it was, you know, in the year you've just, been on leave.
But it was around to the… incubate… incubating classes had some attributes removed, and I thought, we said, we're not gonna do that.
Obviously, I guess it's via an automation, but it's kind of happened, but… broke dependencies, or rather broke code with… permissive dependencies.
Yes. So… have we got any… Ideas, potentially, around avoiding that.
In future, or…
**Brett McBride** 10:30 Oh, you could do that.
**Chris Lightfoot-Wild** 10:30 the…
**Brett McBride** 10:32 I mean, we've certainly got the mechanism to keep them there as deprecations.
If they've been removed, and maybe that's what we… what we need to do. Obviously incubating makes no stability.
Promises, so yes, things can… Ken.
be removed, and we've obviously been eager about using those sort of unstable, SENCOM packages.
Yeah, so…
**Chris Lightfoot-Wild** 11:10 James seems to be like… sorry, go on.
**Brett McBride** 11:12 I was going to say, what I used to do, but haven't done since, sort of, our last refactor, because everything seemed to have stabilized with the split between poor and incubating was actually, you know, I had checks for What has been removed since.
Since the last release, and then we would sort of add them back as Deprecated attributes, and maybe that's what we need to do.
again.
Because that will at least… cause, you know, CI to go red.
on. You know, contrary, without actually breaking.
anything, I think. So is that… is that… The best way forward.
**Paweł** 12:05 Is it possible to do that automatically with the weaver during the conversion of the spec?
**Brett McBride** 12:13 It's a really good question.
I don't… I think it probably depends on whether they would whether they've been filtered out because they're deprecated, or if they were actually removed.
Yeah, it's a good… it's a good… it's a good point. It's worth… it's definitely worth checking.
Yeah, that would probably be preferable.
And probably also to check the policy for removing things from… from incubating, or deprecating them. You know, should they… And maybe they do deprecate them to be removed in one or two releases, just to give us a chance to… Catch up and fix things.
I can take that on as a…
**Chris Lightfoot-Wild** 13:06 It just seems to make using SEMCOM, like, quite risky. The package, sorry, because you could obviously say, I want at least this version of it, and then it's working fine for ages, and at some point, it just… it's a rug pull.
Do other SIGs… Have the same convention, or do they just, like, hardcore the string? Because that's not just gonna blow up.
**Brett McBride** 13:27 No, they… no… I… I think that they… do very similar. Look, it's worth… it's worth double checking, but I… I was copying Java, when I sort of did the last update to incorporate… to do the split between incubating and stable.
It's probably, did the… were the packages removed, or did they go into stable?
Oh, sorry, the, the, attributes.
Do we know?
**Chris Lightfoot-Wild** 14:02 They got renamed, some of them, I think?
**Brett McBride** 14:05 Renamed.
Yes.
Interesting. We're doing alone.
We are moving on. Can't believe that.
**Chris Lightfoot-Wild** 14:23 It feels like the best you could do is probably pin a specific version, but then that doesn't play well with the rest of the.
**Brett McBride** 14:29 And we get…
**Chris Lightfoot-Wild** 14:29 And when it gets…
**Brett McBride** 14:31 stuck. And also, yes, if different packages pin different versions, they're not compatible anymore.
Yeah, it should follow.
semantic versioning.
I'll take that as a… as an action item to… to do that. Try and work out… okay, what to do with that.
But yes, I, I, I appreciate the… Springs.
**Chris Lightfoot-Wild** 15:07 I wonder if our AI agent friends agree on any… a different approach for… Or suggest any different approach for it, as well?
**Paweł** 15:18 I'm wondering, can you use any… Sorry, please, please go, go, go.
**Chris Lightfoot-Wild** 15:25 I'm just saying we've had this a few times, haven't we? So, sorry, come after you.
**Paweł** 15:31 I'm wondering, can we use AI Agent in the CI to track the changes, and then create some issue to update, or… Or, you know, watch the changes in the SEMConf, and even before the release.
**Brett McBride** 15:50 the balls.
**Paweł** 15:51 of the PHP package, we can track for the diffs and generate some reports from… for the contrib trip SDK.
**Brett McBride** 15:59 Oh, yeah.
**Paweł** 16:00 Jess.
**Brett McBride** 16:01 Yeah, that… that might not even need an agent. Oh, sort of maybe we could… we could even just fail to build if a… if an attribute is… is removed?
Although maybe we don't want to keep them around forever, but, as… as part of a… you know, can we just literally check the git diffs if it's… if it's… if there are changes to… to SemConf?
Check for removals and complain, or at least… At least worn, or something.
**Chris Lightfoot-Wild** 16:37 What about also naming… We could namespace the incubating attribute, so you could have, like, 144… Incubating messaging or whatever. And then 145, incubating messaging. If you're…
**Brett McBride** 16:51 Oh, yeah.
**Chris Lightfoot-Wild** 16:51 They're not.
**Brett McBride** 16:52 Keep, keep rolling the boards.
**Chris Lightfoot-Wild** 16:54 I mean, it looks hideous in that you've got a lot of what looks like duplicates, but they don't just go away quickly.
M.
**Brett McBride** 17:03 fruit.
Yeah, well, I might… I might just… get Claude to go and do some research on how other SIGs do this, and just how we can… I mean, the problem's easy to describe.
Yes, those are, those are possible, possible solutions.
**Chris Lightfoot-Wild** 17:24 Cool.
**Brett McBride** 17:25 And speaking of, Chris, I know you mentioned you don't have a clawed, personal account. Did you see the message from Severin in… the check-in channel that, Claude is offering some Ultra subscriptions to… Maintainers.
**Chris Lightfoot-Wild** 17:46 It was a six-month, like, you know, try and get you in the door thing. Was that, was that right?
**Brett McBride** 17:51 That's the one.
Well, I didn't read the terms and conditions, I just heard free and said yes.
**Chris Lightfoot-Wild** 17:58 I interpret it as free for now,
**Brett McBride** 18:03 Absolutely, yeah. Yeah, I would assume that it's… I'm assuming it's going to run out in 6 months, but it may not.
yeah, in the meantime, like, it just saves. I'm just using my employer's credits, which are fine. They seem to be fairly unlimited.
well, at least I can see how much I'm spending, and I know the guy who assigns the credits, so I can just get more.
Yes, but I'm… Yes, certainly.
**Chris Lightfoot-Wild** 18:30 I did see that, yeah, thanks for mentioning it. Maybe I could have a look at it at some point, but… Nope.
Don't want to become too dependent on it, and then I have to start paying for it as well.
**Brett McBride** 18:40 Oh, no, I wouldn't do that. But yes, you're right, it might be hard to do without once you've gotten used to it.
I think I would struggle.
**Chris Lightfoot-Wild** 18:48 I mean, I kind of like not using it when all of the workday is, you know… That way inclined, so…
**Brett McBride** 18:55 Hmm.
Yep.
Yep, understandable.
What else do we need to talk about?
Oh, pal, I have a, I have a pull request in against Distro, to try and generate a… a Docker image.
**Paweł** 19:17 Yes, I saw that, you know.
**Brett McBride** 19:18 Yeah.
It's, yeah, it's not, it's not urgent, but, I'm just, because we, we maintain at my job a large fleet of applications, and I'm trying to push… the OpenTelemetry distro out to them, and I'm just thinking.
how… how am I gonna upgrade?
you know, easily 100 different Dockerfiles. And the idea of, you know, copy from Just seems like a… a very… a much more simplified Way to… to do that. And especially if we do… Tags, like, just, you know, 1, or… you know, once it reaches stability, I can just say, you know.
Take anything that's… anything that's won.
One dot anything.
Yeah, anyway, that's an idea.
**Paweł** 20:13 Yeah, it's… it's a very good idea. I… I never thought that… to do that, so… but, yes. So, I made a review, I found some minor issues. One is maybe more… it's more important. So, if… if you… if you find that it should be fixed, then please… please do. If not, then just let me know, and… and we can… we can merge, but… Sometimes you just have what you know.
Safety in the script, so… nothing goes.
But I guess it should be easy to fix that.
And so, yeah, that's it.
And I'm wondering, I was thinking how to install the packages at all, because we are releasing the tar gzzet archive, and so it's used… Maybe, maybe… Maybe it's… it's a better idea. So I was wondering, maybe we should just, you know, should provide some install scripts which will detect the… the… the… the… the Docker version, I mean, the architecture and…
**Brett McBride** 21:31 Mmm.
**Paweł** 21:31 and so on, and just deploy that, but I think that the copy… copy from is a better idea, it's way, way simpler, so…
**Brett McBride** 21:40 Yeah, and I… it might also be really useful for the OpenTelemetry operator, Think… think that maybe if it, if it was installed, like, the one… my… my PR installs it from… on a scratch image, but… but if it was in, I think, maybe BusyBox, that might be enough, As in… I think, as in a neat container, to just… Just do it. Yeah.
Maybe.
**Paweł** 22:13 But the approach is, is, is, is great, so, yeah.
**Brett McBride** 22:16 Hmm.
**Paweł** 22:17 I'd be… I'd be more than happy to merge it.
**Brett McBride** 22:20 Hmm. Have you… have you spoken much with the, there's… I think there's, like, 2 or 3 people now working on the OpenTelemetry operator and getting PHP in. It was, like, a Michelle Menchiop, and… I think Jerry Long… Possibly, and a third person whose name I can't remember. Have you, sort of, spoken to them much about how How the distro can… Can work with the operator?
**Paweł** 22:48 So, we… we met them.
a few months ago, on the SIG meeting, and we was discussing the approach, so I was… I prefer to use the distro, they were aware that there is a distro, they can use that.
And… but… at some… point, they pushed… pushed for us to use the regular one, the regular extension with the… with everything, and building the… the images.
Because it's in the country repo, we can still change the approach and release the official one with the distro, if… So, but we don't have, you know, the use case. Let's say the success story, so if you use that in your job, then we'll get at least some Some, experience from the field, right?
**Brett McBride** 23:42 Of the distro.
**Paweł** 23:44 Yes, yes.
**Brett McBride** 23:44 Well, I'll let you know. Hopefully, I'll have it in production This year.
**Paweł** 23:49 and…
**Brett McBride** 23:50 Yes.
**Paweł** 23:50 And then we can easily change the approach, so it's just about the repositories, because there was a bit of discussion about… around the repositories, the… Operator, maintainers didn't want to…
**Brett McBride** 24:06 Oh, wow, yep.
**Paweł** 24:07 to push it into the official repository, so I think the code is there, but they didn't want to publish it into the… put it into the separate repository for the image generation, so, yeah.
But the conclusion was to use the… use the regular.
hotel extension and build everything. But I think for this approach, the distro is way better, so…
**Brett McBride** 24:39 Oh, I think so too.
**Paweł** 24:41 It's easier.
**Brett McBride** 24:42 Yeah. Look, we're… we're the maintainers, we have some… we have some… Some say, some influence here, I think.
**Paweł** 24:50 Yeah.
**Brett McBride** 24:51 Yeah.
Yeah.
Yeah, I'm not sure… not sure whether I could prototype anything, Like, writing… yeah. Writing operators is… seems… seems complicated, but
**Paweł** 25:07 So, I have it on my task list in Elastic, so it's planned for current iteration for me, so I have to take care of that anyway, so I'll take.
**Brett McBride** 25:19 You'll be able to install it in an operator.
**Paweł** 25:22 Exactly, exactly, yes. It's about the elastic distribution, but… with my approach is to contribute to the… to the hotel first. So, yeah, I will… I have to… take care of that, and I will try to… To implement that.
So, but now I… it will be a bit more complicated, because there is already an operator for the PHP. So, yeah, I will try to figure out how to change that, and…
**Brett McBride** 25:58 it actually Has actually been committed in… I thought it was still just, sort of, work in progress.
**Paweł** 26:07 So, yes, it's… it's… I guess it's… it's committed, and it… the people are using that.
**Brett McBride** 26:13 Okay, I didn't know that.
Yep.
Yeah.
**Paweł** 26:19 the resource injector projects for the PHP.
I'm not sure if you are aware, there's an.
**Brett McBride** 26:26 What do you think?
**Paweł** 26:27 So, it's a working client.
**Brett McBride** 26:28 Yeah.
**Paweł** 26:29 like the… so it's… it's a LDP Road feature, it's loading the library.
But it's… you cannot use that in the Docker, you can use that in the host.
So, if you have the injector library input in the LD preload.
And this library is being loaded, and it's detecting the processes.
It's trying to inject the agent into the starting process.
**Brett McBride** 26:56 Fool.
**Paweł** 26:57 Java.NET node, and so on, and one of the… Well, one of the community members is also trying to… to achieve that for the PHP.
So… There is a draft puller request for that, and he's using the distro to achieve that.
Because he's just about, you know, fighting the library in the opt folder.
And, and loading the extension into the PHP. So they are using the, the confD folder. There is an environment variable you can set, and then the load the, put… give the PHP the additional folder for the… for the configuration files.
Yeah.
**Brett McBride** 27:45 Okay, I think maybe that's the… That's the process I was thinking about, in terms of, like, auto-injecting OpenTelemetry.
on a… on a… on a vanilla PHP application that has no…
**Paweł** 27:58 Yes.
**Brett McBride** 27:59 previous knowledge of OpenTelemetry.
**Paweł** 28:04 But this feature is not working in the Kubernetes and so on, because you don't have access to the LDP remote from the host, so it cannot inject into the container.
**Brett McBride** 28:15 Oh, fuckin'.
**Paweł** 28:16 But, so it's a host-only solution.
**Brett McBride** 28:19 Oh, okay.
**Paweł** 28:20 It's… it's not working in the container, so that's…
**Brett McBride** 28:23 fine.
**Paweł** 28:24 Yeah, that's a huge limitation here.
**Brett McBride** 28:27 That's not the one I was thinking of at all.
Cool, alright, well, let's, sorry, Chris?
**Chris Lightfoot-Wild** 28:39 No, I was gonna say, sorry, go on, what were you gonna say? I'll let you wrap up first.
**Brett McBride** 28:46 I think we just.
**Chris Lightfoot-Wild** 28:47 I did have something to ask about, but I don't know if you were just about to wrap the whole thing, or,
**Brett McBride** 28:53 Nope.
Go ahead.
**Chris Lightfoot-Wild** 28:57 It was, you say you've tagged… stuff now. So does that include… I had a PR, where you were changing some stuff around for the… Http config, etc, in, declarative config.
Have you… has that settled now? Have you… have you… Does a recent round of tagging include…
**Brett McBride** 29:23 Yes… Yes, if it was committed, yes.
**Chris Lightfoot-Wild** 29:30 there was, like, a sort of, I guess, well, bug report, but more slash feature request, I suppose, that, sensitive, query parameters are being captured. Obviously, I wanted to use the URI sanitizer that was in Contrib.
But it looked like that had drifted in somewhat, and I think yourself and Nevi have been across that, like, PR as well, so maybe comment on that.
I think maybe when EV initially opened the contrib version.
I don't know where you got the… I don't know if you'd seen that elsewhere, or there's some attributes.
That don't seem to be in the spec, but it's maybe, like, proposed or something. But I wanted to kind of build it against the spec one, if it's… available.
**Brett McBride** 30:17 Yep.
**Chris Lightfoot-Wild** 30:17 And update that PR, try and get that moving a bit.
Just remember you said there might have been some master you wanted to dabble with?
**Brett McBride** 30:26 That's true.
**Chris Lightfoot-Wild** 30:27 Have you finished with it now?
**Brett McBride** 30:28 If I'm remembering correct… no, I think I… I think I finished it. I think that… And that's… that's something I need to get back onto, is getting a release candidate out for… declarative config. But I think it's all… I think it's all in there, but as I remember, the HTTP config was just config.
Like, not an actual implementation of doing things with that config.
So what would need to happen, I think, was… is that the… On Tribe.
Package would need to accept Accept that config and use… use the declarative config values to… apply the HTTP.
What everyone's doing.
**Chris Lightfoot-Wild** 31:20 So is… is the thinking there, I guess, that the… The shape of the core one is quite permissive, because it's just, like, an array.
And then it's.
**Brett McBride** 31:31 Again, the shape of the core one is just… configuration.
That can be used by a module, but… So is the, is the core one permissive?
Not sure.
**Chris Lightfoot-Wild** 31:48 From memory, I thought it would…
**Brett McBride** 31:50 I'm talking from vague memory, so, solution.
**Chris Lightfoot-Wild** 31:56 Yeah, let me just quickly, if it's alright, pull it up,
**Brett McBride** 32:00 Not perverted on me.
Yes, it's not a problem.
Aw.
**Chris Lightfoot-Wild** 32:06 I'll stick a link in the chat so you can…
**Brett McBride** 32:09 against… against the authorization.
**Chris Lightfoot-Wild** 32:12 work with that.
I could have put it on the document as well, sorry.
So just… obviously, that's just accepting, like.
**Brett McBride** 32:21 Funny.
**Chris Lightfoot-Wild** 32:21 In an array. It could be whatever.
**Brett McBride** 32:30 Yep. But I just said… Yep, yep, but the…
**Chris Lightfoot-Wild** 32:38 So is that, like, its final form, I suppose, with… with Core? Would it stay as that, and that just then accepts whatever in future?
**Brett McBride** 32:45 I think so.
**Chris Lightfoot-Wild** 32:46 Oh, then…
**Brett McBride** 32:47 If you.
**Chris Lightfoot-Wild** 32:48 If you want to use a shaped version of that, that would be in Contrib.
**Brett McBride** 32:53 That's a good question.
So I've extrapolated, maybe, on that. Tests on the entire time.
Because we didn't show it to the OSC.
at anything. So what happens later.
Why is it picking up for me?
I don't think I'm going to be able to find this.
String, snippets.
Mmm… Yeah.
I've heard enough about it, but it's okay.
It doesn't mean it's not… I'm not going to be able to find this by… Looking around.
The other thing I might look at is… It's, it's, I forget what the word is, but… I'm just checking my notes in the background here, So… Presenting me.
Okay, so we've got an HTTP config provider.
References to the text, and reports, and references to other interpretations of the text.
And, your company, I did a little bank, so… This is not quite human role.
So… No, I didn't realize until after.
I think that.
products.
**Chris Lightfoot-Wild** 35:02 Yeah, the other link is that.
That one in country, isn't it? I don't know if you already landed on that end of the tab, but that's the…
**Brett McBride** 35:08 Is that.
**Chris Lightfoot-Wild** 35:08 More shaped version of it.
**Brett McBride** 35:10 Yeah.
**Chris Lightfoot-Wild** 35:15 Obviously, that one's not as permissive to let new stuff through, or, like, would you need to update the shape of that?
**Brett McBride** 35:20 Yeah, that looks very old, so, that first… Bile, so… yeah, I… I can't… tell you from looking at it at the moment. I'll have to look it up.
**Chris Lightfoot-Wild** 35:37 No, sorry, sorry, I wasn't like a, you know, just a… Curious. And obviously, if it's now… Joined as a maintainer, maybe he's got some… opinion on that as well, because I think that was his… Contribution initially, right?
**Brett McBride** 35:51 Yes it was. It was.
Hello, but I need.
Yeah, the… Is that… Is that the crux of it?
which should you use in Laravel?
**Chris Lightfoot-Wild** 36:10 Yeah, I suppose which one… which is the way forward, like, is… Is the one in… I would have thought that would have been flipped, really, that the one in core is a… More shaped version that you can only use in a specific way.
**Brett McBride** 36:26 Hmm.
**Chris Lightfoot-Wild** 36:27 And stuff in Contrib was more permissive, that new attributes that just appear can be used, but, you know, unexposed, but…
**Brett McBride** 36:35 Mmm.
**Chris Lightfoot-Wild** 36:35 Generally available.
**Brett McBride** 36:37 Yep, yep, yep, I think I understand now.
**Chris Lightfoot-Wild** 36:42 Because ideally, I was trying to think of it, I guess, like the API, I don't want to depend necessarily on some other contrib thing if it's there as part of… Like a core package.
**Brett McBride** 36:55 Yeah.
**Chris Lightfoot-Wild** 36:56 if parameters are there, I wanna… I want to depend on that.
**Brett McBride** 36:59 internet.
Just all contributing.
Because I did… oh, so I've changed this as part of… oh, I changed… 3 weeks ago. Yes, so I've marked this as experimental.
So, why did I do that?
Did that because…
**Chris Lightfoot-Wild** 37:16 So it's not settled in the spec, then, yet, is it? The declarative config?
**Brett McBride** 37:24 bar.
No, I don't think that part of the spec was stable.
Okay.
Okay, so I've marked it as experimental because… Because it's waiting on typed accesses, which is another… part of work.
Possibly.
So possibly that's when that config starts to look… better. It's also possibly just an oversight, so… Perhaps it can be.
**Chris Lightfoot-Wild** 38:19 When you say typed access, is it you're talking, like, a language feature there, rather than some OpenTele.
**Brett McBride** 38:24 Well… it's a… it's a… it's called that in the spec, but the spec was written by Java.
Predominantly. So, no, it's to… it's to… Provide getters, so once you've got a section of the declarative config, I think it's true.
**Chris Lightfoot-Wild** 38:44 Oh, good.
**Brett McBride** 38:44 Methods and mechanisms to… get values out whilst enforcing some type safety, I think is the gist of… the gist of that part of the spec.
**Chris Lightfoot-Wild** 38:56 I guess similar to what's in the Contra version now, where it's trying to give you You know, typed objects.
**Brett McBride** 39:02 Yeah, yeah, and I mean, we do that with dot blocks now, and that's possibly good enough.
For us, and maybe that's the answer.
For us as well, is that, We don't have typed accesses, but we do type checking.
at, Whilst processing.
And parsing the declarative config file, so we know that things are the right type.
So, that coupled with… You know, like a dock block.
Configuration might be sufficient for us, and we don't actually have to create methods to To do that, to fulfill.
you know, a bit of spec for other SIGs that do it in a different way.
Yes, but… but I guess, point still stands, I will go and check.
What?
What that means.
**Chris Lightfoot-Wild** 40:05 I guess the main reason I was asking as well was because the declarative config would obviously be laid out differently if it's been promoted elsewhere.
so it's… obviously, we can update the package, but it would also require someone to Update the declarative config, which… They're probably open to doing anyway, but I guess…
**Brett McBride** 40:29 That's okay.
**Chris Lightfoot-Wild** 40:29 We've shifted it around.
**Brett McBride** 40:31 Yeah.
And so, does that mean that the answer is that sort of… The contrary package should start to shift from one to the other, get the bits from core that are defined in core.
And put some other bits in.
In its own section of… Declarative config for the… for the extras, or drop the extras.
Drop the non-conforming, non-spec bits.
**Chris Lightfoot-Wild** 41:05 Don't… I don't know about that.
**Brett McBride** 41:07 I can figure that out, and yeah, hopefully Nibe can… I want to ceased as well.
**Chris Lightfoot-Wild** 41:17 What was that? Did you say, hopefully it'd be bacon?
**Brett McBride** 41:20 Hopefully Nibe. Sorry, Tobias.
**Chris Lightfoot-Wild** 41:22 Oh! I thought… I thought it was, like, an Australian phrase. I thought you said, hopefully it can be bacon.
**Brett McBride** 41:27 Hopefully.
**Chris Lightfoot-Wild** 41:28 I don't know what that… I don't know.
**Brett McBride** 41:30 Sorry.
You need to clear…
**Chris Lightfoot-Wild** 41:33 somewhere.
**Brett McBride** 41:36 Yeah, okay, so I've got, I'll try to set one up as well. See if I can… Get a better answer.
Or a clearer answer on… on… What the path forward is there, so that you can get moving.
**Chris Lightfoot-Wild** 41:57 Cool, good.
There was still, also, in… did you look at the… security thing in contrary, but I didn't get a response back from… Whoever had followed up on it,
**Brett McBride** 42:10 untrue. Oh…
**Chris Lightfoot-Wild** 42:12 Yeah. There's a secure issue raised around… some Symphony stuff with the HTTB Foundation usage,
**Paweł** 42:21 Because it…
**Chris Lightfoot-Wild** 42:24 The instrumentation actually changes, like, the userland behavior.
**Brett McBride** 42:27 Can I access that?
**Chris Lightfoot-Wild** 42:30 Should be able to. Oh, I thought you were an overarching, like.
**Brett McBride** 42:33 Oh, yeah.
Powers.
**Chris Lightfoot-Wild** 42:36 Advisory is on the left there, at the bottom.
**Brett McBride** 42:39 10 yep.
**Chris Lightfoot-Wild** 42:45 So this is… they said that last month it got open, it was a few weeks since, and I've obviously been away for a little bit, but… Just before the PHP disaster meltdown of the…
**Brett McBride** 42:55 Pizza show.
**Chris Lightfoot-Wild** 42:56 thing.
**Brett McBride** 42:57 Mmm.
**Chris Lightfoot-Wild** 42:58 Yeah, so it was… there's a method in there which it was trying to check some headers for, sort of, malicious… Injection or something.
Yep. And we call a method which then changes state on that object, so then when it's called again by the user, they don't get the same outcome the second time. Like, it throws an exception, which we swallow.
And then… In New Zealand, it doesn't throw anymore.
So, yeah, it kind of creates a whole, in the security.
context, I suppose.
**Brett McBride** 43:36 What? But I suppose that the question's about… Processed now, so… You said that…
**Chris Lightfoot-Wild** 43:44 Yeah, I just wanted…
**Brett McBride** 43:45 Good.
So… so now that I've been through this, I can tell you that, yep, step one is accept it, so… which is just us accepting that, yes, this is… we agree that this is a problem, so it's not published at this point. We then get the opportunity to fix it, patch it, and release a Patch release, and only after we've done that and we're satisfied, does it then get published and become public? So it's still accepting it, it means it's still only visible to You know, you and me and the reporter, and… you know, the security team at, OpenTelemetry.
Yes.
**Chris Lightfoot-Wild** 44:33 It would be a good idea, I guess, for you as well to see this, Pawel, right? Because, you know, you're using all these practices.
You can't.
**Paweł** 44:39 anything.
No.
I don't have anything in Advisory.
**Brett McBride** 44:44 Just like I voted.
**Paweł** 44:44 the vulnerabilities listed, but I don't have anything here.
**Brett McBride** 44:49 Because you're not a maintainer on this repository. So, I think, Chris, you're a maintainer on contribute, and I'm a maintainer on everything.
Because I'm at the… top level. So that would be… that would be Y.
Yes, yeah, I agree, it would be good to have.
To have you on it as well.
I'm not sure how we do that.
I mean, I can make you a maintainer of everything, or of, or of contrary.
I think I have the… Capability to do that now.
Well, I have, because I added… Niveay.
As a maintainer, so… So, I guess I can do that.
**Paweł** 45:34 Okay.
Yeah, yeah.
**Chris Lightfoot-Wild** 45:39 There's a tie him.
**Paweł** 45:41 I can also request somehow, but yeah, it's an additional repository with the…
**Brett McBride** 45:45 Oh…
**Paweł** 45:47 Yeah, but I'm not sure…
**Brett McBride** 45:49 So, weeks ago, you were asking,
**Paweł** 45:52 I just click everything.
**Brett McBride** 45:54 Yeah, we… sorry, I've just realized, so… you asked about being maintainers, or being promoted to maintainers weeks ago, and I… I was expecting that you both would have to create an issue and get sponsorship, but you're already community members, so it's actually something that I can just action. So I can make you maintainers of everything.
right now, like, the entire OpenTelemetry PHP subsystem, which is the core repo, and contribute, and… Distro and instrumentation. Which will give you visibility over all of the security things, and obviously extra privileges as well, whatever maintainer gets you in those repos. So, I am happy to do that.
Right now, actually.
**Paweł** 46:45 Okay, so…
**Chris Lightfoot-Wild** 46:45 Also, we haven't responded in…
**Brett McBride** 46:48 Alright, well.
Way to click.
**Chris Lightfoot-Wild** 46:51 Nivea's responded as well in the chat, saying if you can… if we can bump this meeting back by 15 minutes, then you can… It's outside of… Stand up, so we can… fundamentals.
Do you want.
**Brett McBride** 47:06 Oh, yeah.
**Chris Lightfoot-Wild** 47:07 Yeah, sounds like me.
**Brett McBride** 47:09 Right? Yep.
Yep, absolutely do that. Sim45utc, let's change it. I will… What do I need to do?
I need to change… yep, that's right.
Does everyone agree with that? Pawel, that's okay with you?
**Paweł** 47:30 Yes, yes.
**Brett McBride** 47:31 Excellent.
**Chris Lightfoot-Wild** 47:34 50 minutes of extra daylight before.
**Brett McBride** 47:38 Yeah…
**Chris Lightfoot-Wild** 47:39 Working in the dark.
We had a sprinkling of snow this week, but it all got rained away.
**Brett McBride** 47:54 Oh, that's disappointing.
**Paweł** 47:56 It was snowing here in the morning, just, you know, snowing. It was rain and snow, so…
**Brett McBride** 48:04 Wow, we're just coming.
**Paweł** 48:07 Yeah.
**Chris Lightfoot-Wild** 48:08 Pilar, we don't get as bad a snow as you do in Poland, I don't think.
Our weather's just a bit more, like, average. It's usually wet and dark, but not too extreme either way.
**Brett McBride** 48:21 It's just miserable without the snow.
**Chris Lightfoot-Wild** 48:24 Yeah.
I'm sure that must be why in years gone by, like, British people went and tried to take over half the world, because, like, the weather here sucks.
No one wants to be on silent.
**Brett McBride** 48:45 Yes.
Yes.
**Paweł** 48:49 Okay, so… should I… so I don't need to request anything anywhere, I mean…
**Brett McBride** 48:57 We'll do this.
**Paweł** 48:58 So… You would do as a thing.
**Brett McBride** 49:00 Let's put another one, and… action, like… And… And join us.
Yes, I should have thought of that when I was… processing Nube's request. I was right there.
Sorry.
I just… I thought it was waiting on you two, and that you'd just forgotten, and I wasn't… I wasn't thinking about.
pushing it along. So that should happen.
In the next 5 minutes after I hang up.
**Paweł** 49:40 Okay.
But regarding the winter, I remember last winter, there was at least a few days, and people was ice skating on the sidewalks.
It's a lot of device everywhere.
So there's not only the snow, but also the ice everywhere, so everything was covered to the ice.
**Brett McBride** 50:01 That sounds quite dangerous.
**Chris Lightfoot-Wild** 50:02 Perfect.
**Paweł** 50:03 Yes, it was. Yes, it was very difficult to go outside without, you know… some… you can buy the chains and put it on your shoes. Oh, yes. It's a bit safer, but…
**Brett McBride** 50:16 huh?
**Paweł** 50:17 I was staying at home, just moving, you know, a few meters around, just to buy something in the shops and bakery, but…
**Brett McBride** 50:27 Yes. Yeah.
Wow.
There you go. And I've… I've once saw snow at my house when I was a child.
That's… that's… Yep.
Otherwise, there's, like, one or two mountains, and you have to drive very, very far to see snow right in the middle of winter.
**Paweł** 50:48 Yeah.
**Brett McBride** 50:49 tree.
**Chris Lightfoot-Wild** 50:51 Well, I mean, I'm sure you've seen your fair share of huge, deadly spiders, so, I think I'll say this, no.
**Brett McBride** 50:58 Yes. And snakes, and snakes.
**Chris Lightfoot-Wild** 51:02 Hmm.
Just on… on that thing with the advisory, then… Did you… I was wondering… So that's obviously… it was raised for symphony, but there's a… there's a strong chance, then, that… because Laravel depends on that Symphony package as well, that it would affect that, and possibly other things. And in a similar vein to how the auto route span works in, like, the core part of… Creating a request from globals.
Is that something that we should potentially be able to do in the API? Because a lot of the country packages are trying to reach in and interact with the request.
But obviously if there's a risk that it's gonna modify From a user's perspective, what that object is.
If… the API provided a means of Getting a duplicate of that or something.
Or a safe… safe working copy? Or is it just down to… There's some risk in doing this, beware of it, kind of thing.
**Brett McBride** 52:01 That's a good question. I don't know.
Look, it's certainly worth… worth looking at.
I mean, naively, I would assume that we have to modify the… Main request object.
For auto instrumentation to work.
**Chris Lightfoot-Wild** 52:21 No, so, like, just, if we were just observing it, like, would… in, like, the full query, or whatever method of it, but some… by some method… sorry, that was a poor choice of example, because I used the word method again, but, like, the HTTP burp, is being captured.
And we're calling, like, an object method.
to get that. And if, in that example, that… could modify… the application object before, you know, because we've kind of instrumented ourselves to jump in ahead of them.
**Brett McBride** 52:54 Potentially.
**Chris Lightfoot-Wild** 52:56 Would create unusual side effects.
**Brett McBride** 52:59 Yo.
**Chris Lightfoot-Wild** 53:02 It's pot and parcel?
**Brett McBride** 53:06 Don't know. I mean…
**Chris Lightfoot-Wild** 53:08 Maybe again, just for…
**Brett McBride** 53:09 I take your point that maybe it at least needs to be applied somewhere else, maybe when you understand the problem a bit more fully, we can investigate, and by… Yeah.
Yeah, when you sort of know what a possible solution is, you might have a better idea of Whether that can or should be… Applied.
Elsewhere.
Sort of maybe in the API, as you suggested.
Otherwise, we just copy it.
To everywhere as a… Just as a fix.
Yeah.
**Chris Lightfoot-Wild** 53:54 Maybe that is just the way, but it was just, like, if… are we gonna… is it, like, a class of problem, potentially, or not? I want…
**Brett McBride** 54:02 Or is it a… is it a symphony problem?
Like, is it mutating the request and it shouldn't, or…
**Chris Lightfoot-Wild** 54:15 It looked like the linked tissue was… an intentional thing on the Symphony part, because they were, like.
They throw an exception, but then in their exception handler later, they don't want it to throw a second time, so they've intentionally modified that state internally.
But obviously then, we've come along and added, like, a third call that jumps ahead of those two.
**Brett McBride** 54:38 Yep.
**Chris Lightfoot-Wild** 54:39 it changes that behaviour of the framework.
**Brett McBride** 54:47 Yeah, interesting.
**Chris Lightfoot-Wild** 54:49 But, yeah, investigate a bit more, perhaps. But is there something to do, then, on that? Do we have to… An accept button or something.
**Brett McBride** 54:56 So we don't have an accept button, as far as I know. I had to ask the… I've lost it now.
I had to ask the… Oh, let me think… Well, probably… Probably.
**Chris Lightfoot-Wild** 55:17 Is that potentially why this counts?
**Brett McBride** 55:18 Yeah, actually, I think it should be Carlos, because… As I remember reading it, whoever, like, gets assigned, or whoever picks it up first, so let's say he was on roster 3 weeks ago, technically, he should see it through to completion. There's not, like, a… Hand over as the roster changes.
So… I'll just ping him again on this.
And say… Yes, we accept. If you've checked it, you think, yep, this is legit, like.
And it's all, you know, fairly accurate, and it's a fairly low score as well, as far as CBEs go.
Well, security advisory, so… Yes.
Yeah, that's hard.
probably a reasonable score, but anyway, I think the next step is probably just to ping him again and go, Yes.
Yes, we accept, and we can… Well, I was gonna say, we can take it from here, but we're actually gonna need more help.
Anyway, yeah, but step one is accept.
And then I can help you with the… getting the fix out, or whatever. We'll need to do a release, obviously.
Yeah, but that… that's not… that's not hard, so… It's easy with… as a two-person jobs, so you can have a committer and an approver.
For merge requests, but… Yep.
We've got… we've got enough people to do that.
**Chris Lightfoot-Wild** 56:53 Cool.
Beautiful.
That was it.
All good?
**Brett McBride** 57:05 All good?
Alright.
Thank you for your time. I will… yeah, I'll try and get onto my action items tonight if I can.
So to get answers and get things done.
And, I'll get started on a release as well. If I'm doing it manually, probably just need to look out for a, like, a release prep.
pull request on… on core that'll need to be approved.
Before I can do all the tagging, but that's it.
**Paweł** 57:36 Okay, thank you.
**Brett McBride** 57:38 Oh, no problem.
Alright.
Have a great day, everyone. Catch you… catch you later, and see you online.
**Chris Lightfoot-Wild** 57:45 Cheers.
**Paweł** 57:46 See you guys later.
