SIG: OpenTelemetry PHP SIG
Date: 2026-09-09
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 00:36 Hey, Bob.
**Bob Strecansky** 00:37 Chris, how are you?
**Chris Lightfoot-Wild** 00:39 Okay, Lexi, how are you?
**Bob Strecansky** 00:41 About the same.
**Chris Lightfoot-Wild** 00:43 Nice.
Finally, Olivia.
**Bob Strecansky** 00:48 Sorry, say that again?
**Chris Lightfoot-Wild** 00:49 Bright and early for you?
**Bob Strecansky** 00:51 Oh yeah, nice.
8 AM.
**Chris Lightfoot-Wild** 00:59 Well, what time did you just stop?
**Bob Strecansky** 01:02 I usually start working at, like, 7.30ish.
**Chris Lightfoot-Wild** 01:05 Okay.
Come in especially for us, then, give us some heat up.
**Bob Strecansky** 01:12 Yeah, well, it's like, commuting from my office, or commuting to my office at 8.30 versus 7 is just, like, two completely different beasts.
**Chris Lightfoot-Wild** 01:22 Yeah, traffic.
**Bob Strecansky** 01:25 I go through two of the most trafficked intersections in the United States, from my house to my office.
**Chris Lightfoot-Wild** 01:31 Whoa.
**Bob Strecansky** 01:32 Which is… not, like, with… I went home yesterday, like.
9, and it took me 20 minutes, but it routinely would take more than an hour if I was driving during a rush hour. So I just pretty much try and avoid it at all costs.
**Chris Lightfoot-Wild** 01:50 I'm gonna…
**Bob Strecansky** 01:52 That sounds good.
**Chris Lightfoot-Wild** 01:55 I wonder if we're having Pawel and Brett today.
**Bob Strecansky** 01:59 I'm waiting for our bread, sighting.
**Chris Lightfoot-Wild** 02:03 Me too. Sorry, I cut you off there. You were gonna say something?
**Bob Strecansky** 02:05 Oh, no, you're good. I was having some fun this morning, but I've been unable to merge these PRs.
But we'll see if it works now.
Wow.
I just needed to have somebody else watching.
Seriously.
Wonder if Pawel's gonna come today.
**Chris Lightfoot-Wild** 02:43 Dude.
**Bob Strecansky** 02:43 Daredevil?
**Chris Lightfoot-Wild** 02:46 Good roll.
**Pawel Filipczak (Elasticsearch B.V.)** 02:50 Hey, guys.
**Bob Strecansky** 02:52 How are you?
**Pawel Filipczak (Elasticsearch B.V.)** 02:54 Okay, thank you.
So I have just created another one.
**Bob Strecansky** 03:00 one?
**Pawel Filipczak (Elasticsearch B.V.)** 03:01 Yes.
**Chris Lightfoot-Wild** 03:03 Look at this.
**Bob Strecansky** 03:04 Yeah, I really can't live review for mute.
**Pawel Filipczak (Elasticsearch B.V.)** 03:09 Yeah.
**Bob Strecansky** 03:10 So just updating composer and PHP, so yeah, that's exactly what you're doing with the other ones. Thank you for… thank you for taking on that work.
**Pawel Filipczak (Elasticsearch B.V.)** 03:18 It was a bit boring, but… From time to time, in the background, I was… Picking next and next.
**Bob Strecansky** 03:25 Nice work. The, the only thing that's left is the one that you commented on, Chris.
**Pawel Filipczak (Elasticsearch B.V.)** 03:30 Yes, with this monologue, right? And the configuration issues.
**Bob Strecansky** 03:35 That's like…
**Chris Lightfoot-Wild** 03:35 Yeah, I was hoping we could maybe discuss that, Theater, if we've got any time on the old agenda.
**Bob Strecansky** 03:41 We… I think we absolutely can. Make sure you add it to the agenda.
**Chris Lightfoot-Wild** 03:46 Sweet, I'm gonna do that.
**Bob Strecansky** 03:50 Alright, let's get rockin'. The first agenda item, Paw, what's, I'm going to ask you, what's the B.V dot for in, in your Zoom window? It says ElastaSearchB.V.
**Pawel Filipczak (Elasticsearch B.V.)** 04:04 I don't… I don't get you. Could you… I'm sorry, I crossed the window.
**Bob Strecansky** 04:08 Oh, sure.
**Pawel Filipczak (Elasticsearch B.V.)** 04:09 And could you say it again?
**Bob Strecansky** 04:11 Yeah, your… I think it changed. Is your, your name in the window says Elasticsearch… Elasticsearch B.V? What does B.V stand for?
**Pawel Filipczak (Elasticsearch B.V.)** 04:22 Haha, BB, it's… I guess it's incorporated or something like that in… That's… Yeah.
**Bob Strecansky** 04:29 Got it. Understood.
**Pawel Filipczak (Elasticsearch B.V.)** 04:31 That's… that's interesting, I didn't notice that. Someone added it for me, so…
**Bob Strecansky** 04:38 I was just being observant. Alright, so, making Contrib CI green? Oh, yeah, good work. And I think, like I said, I think the only one that's left open is that one, and we'll talk… we'll talk through this. So, I'll put this in, and maybe we can finally get this green.
Oops, sorry, Chris.
**Chris Lightfoot-Wild** 05:02 No, sorry, my good.
**Bob Strecansky** 05:04 Stupid.
**Chris Lightfoot-Wild** 05:05 You're the anonymous dinosaur.
**Bob Strecansky** 05:08 I guess so.
I am a dinosaur, so… Alright, so we have… We have those. There was a message in the maintainer's channel talking about our old Zoom meeting recordings going away at the end of the year in 2026.
And if you want to… if we want to save any of them, we can.
But, I don't know if we wanna… if we care about saving any of them.
**Pawel Filipczak (Elasticsearch B.V.)** 05:41 I have no opinion on that, so…
**Bob Strecansky** 05:43 Yeah, I don't really either, so I think I'll probably just let them idle away to zero, or maybe I'll download them all, we'll see if I have time, whatever.
**Chris Lightfoot-Wild** 05:54 Is the CNCF as a whole, they're not just grabbing all of them?
**Bob Strecansky** 05:58 I guess not. Let's see, where was…
**Chris Lightfoot-Wild** 06:01 I presume there's a lot of disk space required for, you know, 5 or 6 years worth of… 30 or 40 meetings a week.
**Bob Strecansky** 06:08 Yeah, here's some.
Let's see, they made a spreadsheet.
So I guess, yeah, these are… So, let's see, where is PHP saying?
So we have 63 Zoom meetings, that's a lot.
Hey, Chris!
**Chris Lightfoot-Wild** 06:32 Nice.
**Bob Strecansky** 06:33 Yep, so… I wonder… But that's just for one, I wonder if there's more. There should be more, I would think.
Let's see… Nope.
Is it just… is that just the most recent one?
I guess so.
We'll figure it out. Not really worried about it.
Lost in time.
**Chris Lightfoot-Wild** 07:02 The only ones I've been interested in were the ones before I ever started rocking up, to see what you all used to talk about before it all started going downhill when I joined.
**Bob Strecansky** 07:10 Oh, no. You have been… you've been a wonderful ad. Thank you for continuing to be.
**Chris Lightfoot-Wild** 07:15 You know, like, guys like Tidal and, you know, the early…
**Bob Strecansky** 07:19 Oh, yeah.
**Chris Lightfoot-Wild** 07:20 Yeah.
**Bob Strecansky** 07:21 Yup.
**Chris Lightfoot-Wild** 07:22 Yeah, maybe I'll have to look that up.
**Bob Strecansky** 07:24 That'd be great, a great way to put yourself to sleep if you are having insomnia one day.
Alright, Chris, configuration of instrumentation with SDK API, you ended up a discussion about this.
**Chris Lightfoot-Wild** 07:37 I did, yeah, I think, although… did it tie into what you've just added there? So it's, like, the same discussion?
**Bob Strecansky** 07:44 Probably.
**Chris Lightfoot-Wild** 07:45 Boom.
So, I guess I wasn't sure, initially, if we should have some centralized way of, like, loading configuration. I know… We've got declarative configur… declarative configuration, sorry.
And obviously, if you're using the SDK, that kind of all gets auto-wired in.
Automagically.
I can't remember then… I think there's an explicit rule, isn't there, that the SDK should be separate from the API, so you should be able to just… require, the API as a dependency for a project.
And obviously, by default, everything's no-op, and you can just get on with your life.
And it's detached from the SDK.
Is that about… is that sounding about right?
**Bob Strecansky** 08:35 Yes, it is.
**Chris Lightfoot-Wild** 08:36 So I guess, by extension, I was thinking, should the packages also be the same, that they only depend on APIs that are exposed in that package?
Not via the SDK.
Because if that's the case, I can't see any other way of… using configuration.
In, like, a centralized manner.
Because the configuration resolver was deprecated, but that… Didn't do all the… that wasn't as, like, reflective to load configuration as the new stuff is.
So yeah, I… I just said I wasn't sure that we should add the SDK as a hard dependency on monologue, instrumentation.
Because it broke that, what I thought was a rule in my head.
So firstly, like, do we… is that right or not? Was I wrong? I could be wrong in that, so…
**Pawel Filipczak (Elasticsearch B.V.)** 09:29 I agree that SDKs should not be a dependency for that package, so…
**Chris Lightfoot-Wild** 09:36 Okay.
**Pawel Filipczak (Elasticsearch B.V.)** 09:37 someone can have, you know, different exporters, whatever set, and then they will just fetch everything from the SDK, so it's a huge part of code.
Which is not really needed, right?
**Chris Lightfoot-Wild** 09:51 Yeah.
**Bob Strecansky** 09:51 True.
**Chris Lightfoot-Wild** 09:52 So… the way I kind of looked through, the SDK autoloader, and obviously, very early on, it reaches into the composite resolver… sorry, the configuration resolver.
Which has, like, some composite functionality itself.
Even… so it's… when it's checking it's enabled or not, straight away then it's loading config, so it's very early on in the bootstrapping.
But obviously it relies on its own internal mechanism rather than any API, configuration contract.
And I couldn't see… that there was anything documented in… even… I was looking in, like, Python repos and Java and stuff.
To see if they exposed a configuration API or not. I couldn't see anything obvious.
But obviously in, like, Python, you just had, like, the Environ, sort of global that was pretty prominent.
Whereas we've obviously got, like, the INI files and the environment as well, and different, like, server superglobals, where things could all come from.
So… Should… should there be a configuration API where we centralize this stuff?
And, like, the default would load from the environment and any files.
But then allow extension, so you can wire it in via the SDK, or… Or not, I suppose.
Are we able to add additional things to the API like that, or…
**Pawel Filipczak (Elasticsearch B.V.)** 11:25 We can.
We can do that, so I think that the configuration API would be the best solution, and just implement, you know, a just the… just the, as you said, Environment and INI, and then add possibility to add some plugins.
The problem is that we have this centralized configuration, which… should cut off everything else, right? And we have also the dog pump configuration, which is not really… working… in the SDK itself, it's just a distro.
Bing.
I'm not sure how to… how to solve that, I mean, the order of the configuration loading.
Then, you know, if it will be placable.
and to create some plugin to this API, config API, then we should… Somehow, we cite who… Which plugin has, higher priority.
So, the things we discussed many weeks ago.
**Chris Lightfoot-Wild** 12:33 Yeah, so this goes in the distro, you're… Taking precedence with the configuration, is that right?
**Pawel Filipczak (Elasticsearch B.V.)** 12:40 Yeah.
**Chris Lightfoot-Wild** 12:40 pump thing, huh?
**Pawel Filipczak (Elasticsearch B.V.)** 12:42 Yeah.
**Chris Lightfoot-Wild** 12:43 And your code, I guess, the distro code initializes way before Composer even kicks in, does it?
**Pawel Filipczak (Elasticsearch B.V.)** 12:55 Yes, exactly.
And sometimes, if we can't, then we are injecting into the composer files. I mean, today it is autoload PHP files, so we can just inject the script into the table of the files being loaded.
So, sometimes we are changing the order, doing some hacks there.
**Chris Lightfoot-Wild** 13:14 Is that just a runtime, man?
**Pawel Filipczak (Elasticsearch B.V.)** 13:16 Yes.
So, the modification is not in the runtime, it's when we are generating the… I mean, the system packages. So, if you are calling Composer install.
And after that, we are preprocessing the files.
And injecting the correct order.
But, with this… it can be done with the… with the classic, approach, I mean, a bit of the distro. So, after install, with the after-install script or something, but then it… I think it's… then we will break some rules. I mean, it's not clean solutions, so it's… it's ugly hack.
But I think it will touch the SDK or API, and… maybe… then we… it won't be needed if we produce something which is, you know, which has clean and good API. I will ask my colleague from the… from the Python.
maybe they have sent me, and also from the Java.
And maybe they have some ideas. So, I remember that they had similar issues with the ordering of the config loading, and I'm not sure if… I will ask them how their API looks like.
Maybe they have some ideas.
**Chris Lightfoot-Wild** 14:48 Yeah, that's gonna be really, useful, if that's okay.
**Pawel Filipczak (Elasticsearch B.V.)** 14:52 Right now, I think it's quite a big topic to do that correctly, so it's not easy.
And, Maybe we should also try to update other packages, other, like, in this country repository. Try to use that, make use of that, and then it will be clarified if it's easy to use or not easy to use.
I mean, this new API, and if you… if we can solve all of the… all of the problems, because I think it's, like, the… it's a very fragile component. If you do some bad decisions, then it will affect for a long time.
And it may kick us. Now, everything is totally, you know, it's a huge mess up. In some packages, the getEnf is being used, in some other, the config API is being used, so… Unless.
Yeah.
**Chris Lightfoot-Wild** 15:48 I did notice as well, there was, a couple… so the way loads currently differs, and there's two different, like, environment variable loaders.
And two different interoaders as well.
Which… they looked like they had slightly different… structure to them. Like, they might… one might be doing a bit more than the other.
But it gets swapped out, so it's… yeah, maybe it's a bit messy, isn't it?
And I guess we could ideally… Reduce that down to one of each.
Yeah, if you have a chat with your colleagues then, I guess, and…
**Pawel Filipczak (Elasticsearch B.V.)** 16:23 Yeah, I will ask them. So, I remember that one of them, I stopped working around that, especially in case of remote configuration.
So, yeah, but I lost… I went to vacation and then lost touch. I'm not sure how it evolved, and if they continue to work around that or not, so I have to refresh my knowledge.
**Chris Lightfoot-Wild** 16:50 Does the distro shadowing thing pose any problems with stuff like this, then? If you're wanting to introduce a configuration object.
The shadowing functionality of the distro for hotel packages.
Would that cause any issues?
Or can you exclude specific…
**Pawel Filipczak (Elasticsearch B.V.)** 17:10 I can exclude any class, so I can just exclude any class, but then it's sometimes difficult to reach, because the namespaces are not from the root.
So they are just taken from the… from the shadow namespaces, so if you want to access something from the… from the outer space, I mean, from the root of the… from the unnamed, let's say, from the beginning, then you have to write some rules. But, yes, it's… everything is possible, so…
**Chris Lightfoot-Wild** 17:41 And I guess your extension code… Is firing before the autoload has been registered.
**Pawel Filipczak (Elasticsearch B.V.)** 17:48 Yes.
**Chris Lightfoot-Wild** 17:49 Yeah.
I guess there's no other hooks after that, is there, that you could intercept?
Would benefit that?
So…
**Pawel Filipczak (Elasticsearch B.V.)** 18:02 Source, please continue.
**Chris Lightfoot-Wild** 18:05 No, I was only gonna say, I'm sure you know a lot more than me about the internals of that, so…
**Pawel Filipczak (Elasticsearch B.V.)** 18:10 So, if… from the… from distro extension, you can do whatever you work… you want, so it's… you can just… we have a… We have a bootstrap which is triggering everything, and then we have a… also hook, which is triggered before the autoload.
So, you can… Put some code before the autoload starts, you can put something afterload starts, so… A bit of trickery, though.
**Chris Lightfoot-Wild** 18:39 Okay.
Yeah, I just don't know if I should play around with something, or just wait until you throw those questions at your colleagues and see what they come back with, and So, happy to…
**Pawel Filipczak (Elasticsearch B.V.)** 18:54 Can you ask them today or tomorrow how they manage that? Yeah. I remember that I, I have to, I have to take a look into Meetings notes from our, our weekly sync.
And to… I guess I will find something, and I will dig a bit. I will… How far they went, all that.
Because it's a very similar issue for the other technologies, how to mix the configurations.
**Chris Lightfoot-Wild** 19:22 Okay. I'm glad I wasn't just overlooking something then, because I did go to the OpenTelemTelemetry specification repo and looked up configuration. Obviously, it talks about the declarative configuration, but totally skips on any uniform way it should load.
config, outside of that, well.
I don't know if that was a lacking thing on the… or left to the… Each individual language to decide.
Mmm.
Cool.
**Bob Strecansky** 19:54 I know from listening to some of the other SIGs talk about that in the maintainers meeting, it's like, there's a constant… ankle biter, and I think that they're ambiguous on purpose, because I think they know languages have very, very different explicit ways that they handle these, configuration loadings.
So I think that's working as intended, but if you have questions about that, they're, like, unbelievably receptive in the issues for GitHub there.
**Chris Lightfoot-Wild** 20:23 I guess as long as we get a nice enough API that configuration can be accessed via, then the SDK can wire it in however it likes.
Yeah, it's a uniform way of accessing it across all the packages.
**Bob Strecansky** 20:37 That's right.
**Chris Lightfoot-Wild** 20:38 It'd be awesome.
Well, alright, well, thanks then, Paul.
**Pawel Filipczak (Elasticsearch B.V.)** 20:43 I will come back to you, I hope, soon.
**Chris Lightfoot-Wild** 20:48 Sounds good.
**Bob Strecansky** 20:49 Alright, last thing on the agenda, renovate and release. I'm… I was waiting to see if Brett wanted to do the honors for the release, but he didn't respond, so I'll probably just merge a bunch of the renovate PRs that are passing CI after Hal's last PR gets merged and then released. I feel like that's a good chance for us to make sure they're green.
**Chris Lightfoot-Wild** 21:09 Just for instrumentation, that one, is that a…
**Bob Strecansky** 21:14 I'm sorry, ask your question.
**Chris Lightfoot-Wild** 21:16 Was that more specifically for instrumentation? Could we do just the instrumentation, at least first?
**Bob Strecansky** 21:22 We could do just the instrumentation first. I'd like to do them… I usually like to do them all at the same time, just so that they all get released at the same time, but if we had to do the instrumentation, we could. I'd prefer to do all three at once, just so that they all get At least, close to the same time.
It's just easier account… easier accounting for me, rather than, like, oh, we released instrumentation on the 9th, and then we released Contrib on the 10th, and so on and so forth. I'd rather just say, yep, we did a release of all of them on the 10th.
**Chris Lightfoot-Wild** 21:53 Because I've been maybe breaking that mould a little bit by just doing ad hoc whenever, you know, I think someone needs this one, I'll just tag it, I was able to get to do more of it.
**Bob Strecansky** 22:05 No, that's quite alright. I just think… That, that's the pattern that I have followed. It doesn't necessarily need to be the pattern that others have followed.
Especially if you want to keep up with it yourself, so…
**Chris Lightfoot-Wild** 22:18 I guess it would be awesome, obviously, to have the automated tagging kind of kick in, but would… maybe…
**Bob Strecansky** 22:23 Yeah.
**Chris Lightfoot-Wild** 22:23 What's up?
**Bob Strecansky** 22:25 I don't think we're that far away from it, right? Once the repos are green, then we can do the whole… Merge train slash… automated release thing, but I think that getting it green… thank you, Paw, I feel like I gotta, like, give you a high-five over the internet, like… Great work with that.
**Pawel Filipczak (Elasticsearch B.V.)** 22:43 How do… how do you choose which… which issue is, it should be released.
I mean, if you are managing some issues, right?
**Bob Strecansky** 22:54 Yeah, I think the right answer to that question, unfortunately, is what your heart tells you, and we don't have, like, a specific release cadence or reason to release, it's just been ad hoc, which I think is a mistake. I think what needs to be done more consistently.
**Pawel Filipczak (Elasticsearch B.V.)** 23:07 Maybe we can introduce some label, let's say release candidate or something like that, that the issue is breaking or adding something which is spectacular.
Oh, yeah.
**Bob Strecansky** 23:17 I think…
**Pawel Filipczak (Elasticsearch B.V.)** 23:17 And then… then we can filter out which issues is… is not released yet, right, from the… from the last release. Maybe it will make our lives easier, because now I… I remember that I had some… these headers capturing in the… in the contrib.
And there are a few packages where I added that, and now I don't really remember which I modified, and which was released, which wasn't, so…
**Bob Strecansky** 23:47 Yeah, I think I see that as a double, two-sided coin, doing release candidates.
Do I think it's the right thing to do? Absolutely. Does it add just, like, an even more friction in our already annoying release process? Yes. So I think that I would love to get to the point where we're doing more release candidates, but I think we probably need to get our… like, doing it all manually stinks, too, so I would really like to get our release process to a place where it happens.
Not by me clicking the enter button 50 times to release each of the packages individually, and blah blah blah, so… I think that's something we can definitely consider in the near-term future. I want to make sure that we have CI agreeing before we do that, because that will just… I feel like that will open up a lot more avenues for us.
**Chris Lightfoot-Wild** 24:36 Cool. Are we still happy with continuing on that, split? I've not done it for a little bit, sorry, but, I see some of the changes you've done recently are just obviously leaning on the existing CI, but you're not against I mean, still splitting them out into individual ones, partly.
**Bob Strecansky** 24:53 I haven't… I haven't heard any yelling about it, so I think that it… it's fine.
I appreciate you doing that, because I think that will help.
give people a little bit more gumption around the work that they want to do, and not have to worry, like, oh man, am I impacting too many people, or whatever.
Should make a thing.
**Chris Lightfoot-Wild** 25:12 Let me just think of one more thing, sorry to add on. Is that right?
**Bob Strecansky** 25:15 You're alright, we got plenty of time.
**Chris Lightfoot-Wild** 25:19 the, whoa.
**Bob Strecansky** 25:24 Oh, yes, this is a more workflow.
**Chris Lightfoot-Wild** 25:28 what the… Sorry, I'm not going to discuss it so much here if I'm just opening it, I suppose.
Yeah, the, it requires an explicit tag, or reference. So I did do, like, a proof of concept PR the other day.
And Zizmo just kicked off at me.
Which…
**Bob Strecansky** 25:52 Where is this?
**Chris Lightfoot-Wild** 25:53 in Contrape,
**Bob Strecansky** 25:55 Oh, sorry.
**Chris Lightfoot-Wild** 26:06 Who else?
**Bob Strecansky** 26:06 That's you.
This one?
**Chris Lightfoot-Wild** 26:10 That was it, yeah.
**Pawel Filipczak (Elasticsearch B.V.)** 26:11 You have to close and reopen the PR, then it will start again.
**Chris Lightfoot-Wild** 26:16 No, it's… it's just unhappy with what I'm trying to do. Like, it objects.
**Bob Strecansky** 26:24 Yeah, I think this… yeah, that makes sense. It wants you to do… it wants… like, they've been really, really, Adamant about wanting to have explicit, Shaw hash has 4 versions, rather than D.
**Chris Lightfoot-Wild** 26:40 Yeah, so that just means either we… we'd have to decide that we're happy with, like, the workflows as… as they are at the second, and at least tag contribrib.
So we've got the.
**Bob Strecansky** 26:50 Oh, I see what you're… I see what you're saying. Got it.
**Chris Lightfoot-Wild** 26:53 them into the OpenTelemetryphp org, so that we can tag it there, and it's not changing every single time head changes.
Because at the moment, you know, you merge this, and then it'll open another PR going, oh, you're a commit behind.
Like, forever.
**Bob Strecansky** 27:07 Yeah, that's true. I don't know that… I don't know that I've come across that before. I wonder if other SIGs have.
**Chris Lightfoot-Wild** 27:17 I think it's our composer ecosystem not favoring.
**Bob Strecansky** 27:20 Oh, yeah.
**Chris Lightfoot-Wild** 27:21 That's right.
**Bob Strecansky** 27:23 completely.
**Chris Lightfoot-Wild** 27:23 It's a bit of an abuse, isn't it? So… Even…
**Bob Strecansky** 27:26 Bit of an abuse.
**Chris Lightfoot-Wild** 27:29 Even with the tagging thing, I'd be interested, like, getting it green as… One thing, but then, like, how do you even decide to split and tag at the same time for a specific one?
Thank you.
**Bob Strecansky** 27:39 You know, I wonder if there's, like, a specific… there's a more rule for that, too. I haven't read enough about it yet. Maybe that's some research that we need to do.
**Chris Lightfoot-Wild** 27:49 Hmm.
I've seen stuff where, like, Symphony or Laravel have monorepos, and then they decide to, like, tag And split everything at the same time with the… As I understand it.
One of the things that, like, split off from those, like Laravel's Octane, doesn't sit as part of the framework package, it's its own thing, so obviously they release that hasn't went.
But everything else from the framework is split at once. I guess we're not going to do that, because they're all… separate packages.
So…
**Bob Strecansky** 28:24 They are.
**Chris Lightfoot-Wild** 28:25 Joe.
**Bob Strecansky** 28:26 I will… I'll do some reading about this more and see if we can, like, exclude this for… Something, or if we could… if there's something else we could do.
**Chris Lightfoot-Wild** 28:37 Okay.
Thank you.
**Bob Strecansky** 28:40 Well, beams.
Right.
Anything else y'all want to go over?
**Chris Lightfoot-Wild** 28:46 Well, on that release then, because Nick had asked the other week, in the… Slack channel. Can we go back to it and say, I guess it's in the works, or… I know you've already said there's no explicit date, but, like, we could say we're doing it this week, or…
**Bob Strecansky** 29:00 Yeah, I'll do that. I'll say that now. I will plan, I'll just say we're planning on releasing by end of week.
**Chris Lightfoot-Wild** 29:09 Cool. And I thought of one more thing, and I'm really sorry. I looked at the, one contributor, I can't remember the name, had, opened an issue in the OpenTelemetry docs.
**Bob Strecansky** 29:22 Oh, yeah, the one that had, like, yes, I saw that.
**Chris Lightfoot-Wild** 29:25 Yeah, and I like.
**Bob Strecansky** 29:26 maintenance.
**Chris Lightfoot-Wild** 29:27 Yeah, but if…
**Bob Strecansky** 29:27 B.
**Chris Lightfoot-Wild** 29:28 Yeah, I like the initial issue template, where it says.
I have or haven't used AI, and I do understand or do not understand the work that I'm sort of.
**Bob Strecansky** 29:38 Oh, this one?
**Chris Lightfoot-Wild** 29:40 I wondered if we can, like… should we just take that and use it in our…
**Bob Strecansky** 29:44 100%, I think that's a wonderful idea. Just… I think being transparent about that is always good, right? Like, it's fine if you use it, but just having other people know that you use AI to have it happen, I think that's a good idea. We should put this in our repos.
**Chris Lightfoot-Wild** 29:59 Cool. I don't mind, if we're just taking it verbatim, then I can just, do that in.
**Bob Strecansky** 30:04 Yeah, the issue template.
Or no, not the issue table, but, where is that? That's in… Where's it called?
**Chris Lightfoot-Wild** 30:13 But the issue template directory, yeah.
**Bob Strecansky** 30:16 Yeah.
No, this is for issues, not for pull request templates.
**Chris Lightfoot-Wild** 30:20 Boop.
Oh, okay.
**Bob Strecansky** 30:23 Trying to remember where that is.
We'll find it eventually, but yes, that's a good idea.
**Chris Lightfoot-Wild** 30:33 Well, I can… I can do that if, if we like, if we're happy with that.
**Bob Strecansky** 30:39 Yes, please, please and thank you.
**Chris Lightfoot-Wild** 30:40 what, contra… men… instrumentation, when you… Well, you want Distro doing Pawel? I can… I can try and open a PR for that, if you like.
**Pawel Filipczak (Elasticsearch B.V.)** 30:53 Yes, please.
**Chris Lightfoot-Wild** 30:55 Cool. Yeah, I'll do that.
Sweet. Thank you very much. I'll stop thinking of things now. Apologies.
**Bob Strecansky** 31:03 All good.
Alright.
We'll, we'll catch y'all next week. Thanks, everyone.
**Chris Lightfoot-Wild** 31:10 Yeah, Scylla.
