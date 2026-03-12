SIG: PHP SIG
Date: 2025-10-22
Duration: 27 minutes
Zoom Recording URL: https://zoom.us/rec/share/qfF7J6IU7gg0dLKRNdgieAEv3TLgr-91MaZH4D39PhoGpqqUatFStaYW9itGAqrc.3GGUvZC0izyWZLqz
============================================================

## Zoom Recording Transcript

**Chris Lightfoot-Wild** 01:05 Hello.
**Sergey** 01:06 I'll get that done.
**Pawel Filipczak** 01:11 Hey guys.
**Chris Lightfoot-Wild** 01:13 Hey, Adrian.
**Pawel Filipczak** 01:14 I'm okay, thank you.
Oh, I am.
**Chris Lightfoot-Wild** 01:18 Yeah, or that's cool.
**Sergey** 01:22 Getting colder.
**Chris Lightfoot-Wild** 01:24 Processor?
**Sergey** 01:25 You're from Manchester, right?
**Chris Lightfoot-Wild** 01:27 Near-ish, yeah. Yeah, it's colder, if that's what you said, Zoe.
**Sergey** 01:33 Sorry, what'd you say? Sheer?
**Chris Lightfoot-Wild** 01:36 Pardon?
**Sergey** 01:37 When I ask, are you from… you're from Manchester, right? If I remember correctly.
**Chris Lightfoot-Wild** 01:42 I'm near Manchester, I'm in… Oh, near…
**Sergey** 01:43 Okay.
**Chris Lightfoot-Wild** 01:44 Yeah.
**Sergey** 01:45 The place called Shire, like, like… Yorkshire.
Yorkshire. Okay, yeah.
**Chris Lightfoot-Wild** 01:52 Okay.
**Sergey** 01:53 I thought it was, like, just Shire. There's lots of Shires in England. Yeah, there are Shires? Oh, okay, so he didn't make that up?
**Pawel Filipczak** 02:03 Do you have a Terrier?
**Chris Lightfoot-Wild** 02:05 Do I have a terrier, a dog? Yeah. No, like a Yorkshire Terrier.
**Pawel Filipczak** 02:10 Yeah.
**Chris Lightfoot-Wild** 02:11 No, but I like to eat Yorkshire puddings. Amazing.
You guys had that, Yorkshire Puddings, do you know what that is?
**Pawel Filipczak** 02:19 It's not…
**Sergey** 02:20 Not those meat pies, right? Like, not shepherd meat pies, actually some sweet, some dessert.
**Chris Lightfoot-Wild** 02:25 No, it's like a… it's like battered, like a little, it's a server thing.
**Sergey** 02:31 Oh, okay, so South is…
**Chris Lightfoot-Wild** 02:33 We're roasting a…
**Bob Strecansky** 02:34 I thought it was a meme. I didn't think British people actually ate that.
No, yoga's their thing. No, I know it's a real thing, but I thought it was, like, one of those, you know, like, cultural appropriation things, like, oh yeah, everybody eats that, like, you know, but that's cool, I'm glad to hear that it's a real thing.
**Chris Lightfoot-Wild** 02:50 Yeah, no, they're really good. Worth a try if you have a… I don't know if I've seen one in America, but, you know, it's just like… batter and fried, yeah, it's nice.
**Bob Strecansky** 03:00 Turns out… turns out fried food, typically pretty good.
I come from the land of fried foods.
**Chris Lightfoot-Wild** 03:09 And homemade southern comfort foods, though, is it? Big in Georgia?
**Bob Strecansky** 03:14 Yeah, yeah, Southern comfort food is very… I'm a Southern transplant, and it's very fascinating to me.
It's, barbecue is, like, part of the culture in the Southeast, and… that's, like, if y'all haven't ever had real barbecue before, it's really cool. And it's funny because, like, each state has their own type of sauce that they put on the barbecue. Like, South Carolina is ketchup-based, North Carolina is mustard-based, albeit, mayonnaise-based.
And, like, it's, like, it's very strange how, like, different locales just do the same thing, but just, like, with a slight nuance.
They're all awesome, though.
**Chris Lightfoot-Wild** 03:56 Love it.
**Bob Strecansky** 04:01 Okay… Do we expect anybody else today?
**Chris Lightfoot-Wild** 04:09 tomorrow.
**Sergey** 04:11 Most of the people, I only see them here or something.
**Bob Strecansky** 04:14 Yeah, I think…
**Sergey** 04:15 I think we have.
**Bob Strecansky** 04:18 Yeah, it's like, who's gonna be here today?
Alright, y'all can see my, screen?
**Chris Lightfoot-Wild** 04:24 Yep. Yep.
So…
**Bob Strecansky** 04:28 The only agenda topic that I had for today is… the, one of the other people in OpenTelemetry opened a quote-unquote CVE, which I think is, like, one of the most goofy ones that I've seen so far. So, in our GitHub actions.
They, we use particular versions of the GitHub Actions.
But the supply chain issue that they had raised, I don't know if y'all can see this or not, I don't know if this is, like, maintainers only, or if y'all have the ability to see this, but it's like, they want us to pin the explicit Shaw as part of the GitHub action, so that a supply chain attack can't Inject itself into our… Library.
**Sergey** 05:15 So, I remember that that issue was raised a couple of months ago, and it's some bot that raised it, right? And I think the assumption was we can ignore it, but is there now people behind it that want to enforce this approach with Sha?
**Bob Strecansky** 05:30 It's funny, because, like, I was looking at some of these, yesterday, and it looks like some of them… that Dependabot has created have an explicit SHAL associated with them, and then other ones that Dependabot also created… oh, maybe that's not a good example.
Yeah, like, this one… this one is also Dependabot, and it doesn't have a SHA associated with it. So it seems… I'm… I want to follow up with… I want to follow up with somebody, I'm not sure who, to see why Dependabot would be having Different behaviors for the same workflow.
**Sergey** 06:05 But is the bot that complains itself to depend a bot, or the bot that flagged it as a security issue is different?
**Bob Strecansky** 06:13 No, this is a… this is a real person.
**Sergey** 06:16 Okay.
**Bob Strecansky** 06:18 Yeah.
I'm trying to take all of… I'm trying to take all of our security CVs very, very seriously, as we should, but this one just feels… it feels like somebody's searching for a problem. Like, yes, we all know supply chain attacks are a thing, but… if somebody did that, then they could probably, like, do something else, too. I don't know, it just seems kinda…
**Sergey** 06:40 But how are we gonna upgrade? Like, how we will find, let's say.
How are you even gonna find this SHA for this version 3.81? And then if you want to upgrade some other version, how do you find those SHAs that you can test?
**Bob Strecansky** 06:54 That's… that's why I want to ask somebody from Dependable. I might just ask in the Hotel Maintainers channel, because… I definitely don't want to get in the business of being responsible for upgrading these and upgrading the Shaw by looking at the pa- like, manually looking at the package and copying it over and, like, error-prone and… all these other things, so that's on my list of things to do after this meeting today, is to, like, follow up with others and see how they've remediated this problem, because it seems like It just seems like it's very inconsistent.
I'm wondering…
**Sergey** 07:26 The whole thing is that the whole vulnerability of supply chain is the fact that somebody penetrated supply chain. It's not like you suddenly go and take some stuff that is not from the trusted supply chain. It's that… so, the whole issue is that how fast can they discover that somebody penetrated it, and so people will not try to use it, right? So the whole point of SHI is essentially You're not gonna automatically go and use the latest version, you will be pinned some older version. But then, if, at the point when supply chain is already compromised, you go and upgrade to the latest, right? And even if you use SHA, But the latest thing, the latest artifact on the supply chain is already compromised, so it doesn't matter if it's Xiao or not.
**Bob Strecansky** 08:10 I… yeah, I agree with you. I'm… I'm in the same camp as you. To me, it feels like, it feels like two separate, like, valid concerns, right? Like, if you pin an explicit SHA, and that SHA has a known vulnerability, then even when you upgrade, like, even as you upgrade that vulnerability, you'll probably still carry over. But using latest also has… The supply chain vulnerability, because if you use latest, then somebody could get into the supply chain and then… You know…
**Sergey** 08:37 Yeah, so the question…
**Bob Strecansky** 08:38 So what, like, I'm just trying to understand, like, what are they trying… so they consider supply chain more important to avoid? Like, so they say, okay, so people need to wait, some kind of, like.
**Sergey** 08:50 quarantine period, for any upgrades to the dependencies, after it's kind of, like, whatever could have been, you know, vulnerabilities already discovered. And, and this is sacrificed, the other use cases sacrificed, right? With the fact that you will use latest, then if something is discovered in old things, you will be already using latest where it's already fixed, right? You will not be using latest because you pinned the shot.
**Bob Strecansky** 09:16 Yes, I agree with all of your points, and that's why I want to get more clarity. I think it just feels… it feels like a security researcher trying to find something to complain about, but… We'll, we'll get it fixed up.
**Chris Lightfoot-Wild** 09:28 The only other thing on that, if you look at the pull requests, there, Bob, there's one… it's one of the other numerous ones that come in, like, daily, the code quality ones.
It… one… there's one that's emerged at the top there. So that's… that says it's upgrading from 430.8 to 430.9, and if you look at the diff, it's actually… like, the comment has lagged behind.
And I can't remember where it was, but I'd found somewhere that was suggesting there's a, like, a problem with this, where you're supposed to manually update the comment as well, but it hasn't done. So it just kind of puts it even further out of whack. Like, it's obviously… you could go and figure out what that shower was, but it's effort.
It would be good if, obviously, if that was, something that was fixed as well, because then you could actually…
**Sergey** 10:15 So that's a technical problem, I agree with you. But then, if you have things like that, that run regularly, every day, and upgrade you to the latest version anyway, just with SHA this time, then you will take the latest that is already compromised, right? So you're kind of, like, not even… you introduce an additional complexity without even enjoying.
**Chris Lightfoot-Wild** 10:35 If you just trust the benefits of your…
**Sergey** 10:36 That is, kind of the quarantine period, right?
**Chris Lightfoot-Wild** 10:39 Yeah.
**Sergey** 10:40 You're upgrading every day anyway, so if it's a zero-day vulnerability, you will take it.
**Chris Lightfoot-Wild** 10:44 Yep.
**Sergey** 10:48 I mean… Maybe some people are capable of explaining what's this whole… how it's supposed to work together.
But, yeah.
**Bob Strecansky** 10:57 Yeah, I'm cautious, but I am really interested to understand what, like, the goals and intentions are, and the way that whatever. So, and yeah, anyway, I'm planning on following up with this today. I'm just… I wanted to make sure that y'all knew.
**Sergey** 11:10 I don't know if you're familiar with a guy called, Prime something? Primer? Prime? He's on YouTube.
**Bob Strecansky** 11:16 Prima… primogen.
**Sergey** 11:17 Pramogen, Pramogen, yeah. He addressed this a couple of times, and he always mentions this guy that invented the language, like, Odin, I think, that he mentions that the solution is to have as much dependence as possible in the core library.
So essentially, it's essentially kind of like delegating this responsibility to some kind of, like, trusted authority, like core developers, and they will upgrade the library when they, you know, to make sure that it's not compromised. Because if you take independency left and right from, you know, every deacon Herod, this is how you say it?
Then, yeah, you have a much bigger chance that you will, you're essentially taking the least common denominator, security-wise, yeah.
**Bob Strecansky** 11:56 Oh, a million percent. I think that the fewer external… unfortunately, as software developers, we all know, you need to have external dependencies, because I'm not rewriting Guzzle just because I want to avoid the external dependency, and I think you always… it's always a careful balance, right? You have to use the libraries that make sense for your project, but you also have to be conscientious to Keep your footprint small and your output, you know, all these things, so… Long story short, I will follow up, I will let y'all know next time what happened.
Alright.
Anybody else have agenda topics before we walk the board?
**Sergey** 12:33 I had a question, Janelle, but we can leave it. Yeah, please go ahead, Chris.
**Chris Lightfoot-Wild** 12:37 Well, no, mine was only just to touch on… we built up some from last week, so I don't know if we wanted to talk about some of those now, if you've got the answers, Bob, or… do that later, but if Sergey's an actual problem, like, right at hand, please do go for Sergey.
**Sergey** 12:53 I had a small question, but we can do it after the regular steps that we do, like…
**Bob Strecansky** 12:59 Oh.
**Sergey** 12:59 It's, mmm… Alright.
**Bob Strecansky** 13:03 No, we can… we can… we can rock… we can rock through these pretty quickly, I think. I don't think there's a whole lot of new stuff.
Alright, 22 million, let's go.
New pull requests… Looks like Brett's working on the declarative config.
Update… And that was the most recent thing. Chris, you had this from 2 weeks ago, is that still a work in progress?
**Chris Lightfoot-Wild** 13:43 I need to just pick it up again. I think, it didn't get shut down, but there was some conversation, and Brett's actually commented on it as well, so… Great.
Yeah, there's potentially some change that I could make.
**Bob Strecansky** 13:57 Alright, if you need help, if you need, review or help with that, let me know.
**Chris Lightfoot-Wild** 14:01 Cool, thank you.
**Bob Strecansky** 14:02 Contribute… looks like there's a README update and some chores.
Take a look at those… Instrumentation, there is some GitHub Actions, okay, well, I'll take a look at all those later today. Here… No, thank you.
Cheer.
Something new here.
Okay, so I think that's… It's all the open stuff we have.
Alright, Chris, back to you.
**Chris Lightfoot-Wild** 14:42 Well, unless… Sega, did you…
**Sergey** 14:45 Let me show you guys, maybe you will have quick advice. Would you mind if I share, just to show you guys what… So, we encountered an issue that kind of, like, broke our functionality, let me show what that was. So, there was this change in SDK.
We didn't follow, unfortunately, we didn't have a test that caught this regression from our point of view. So, at some point, the resource detector for the SDK was this line added that overrode the attributes for telemetry distro.
name and version. And I assume it comes… there is a reference here, And it comes from this change in the documentation that says that, distro name should be set to the, this kind of string.
So, when it says should, it's not clear, like, should it consider if it's overridden from, like, the configuration, like, by environment variable, or should it always… so, the way it works now, it overrides, because of the sequencing of the… the way those detectors are registered.
queried, the SDK will always be here, so it will override the environment that says here. And even if you try to register it different via the SPI, Then it will not help, because SDK will still override it.
So, I just wanted to ask, so we would like to set it to something different, because the language here, it's a little bit tricky, I guess. It says if it's official auto instrumentation agent, right?
So, my question is essentially, how can we tell SDK that it's not an official lever there?
Because the way SDK detects that is by just querying if this extension is loaded.
But we had to fake this. We had to, even in our extension, we still say that this extension is loaded, because all the instrumentations exactly check for this as well.
So, if we will not fake it, then instrumentation will also not load, right? So, we would actually prefer for this to be false here.
But, you know, we can, of course, do this in some kind of trickery, but we cannot allow this to be false for the instrumentation, because then all the instrumentations that rely on the hook in extension, they will not work.
So, maybe there is a different solution for that, but… so I was just wondering, maybe we can, Change the order, maybe we can put this one as the last.
So it will be capable of overriding, or maybe we can just check here that if, If this resource is already set, then we should not override it.
So Essentially just depends how we interpret this language, like, when it says should, does it mean that it should also enforce it, even if it's kind of, like, overridden somehow externally?
We just want to find a way to override this somehow, hmm?
**Bob Strecansky** 17:48 Yeah, the, from… they talk about the semantic conventions a lot in the maintainers meeting, and their, their verbiage is very, very intentional with stuff like this. When they use the words like should or can, it means… it doesn't have to be that way, but it's, like, a very strong recommendation.
So, the way that I interpret this, the letter of the law is, like.
We definitely can, like, we could definitely do that conditionally, or we could do it just… whole hog, sort of like we're doing now, right? Like, we… like, overriding it every time is definitely a piece… it's, like, definitely… Valid and plausible, but… to me, it feels like we should have that, like, that, second option that you talked about with conditional logic. I don't think we should change the way that the, which they, load. I don't think… we didn't think we should change the order in which they load, but if you want to add a conditional around, like, 40… like, around 49, then that's… that seems like a reasonable…
**Sergey** 18:46 So, to add some other condition that can be overridden, we can tell it that it's not an official, how it's called here.
**Bob Strecansky** 18:55 Yeah. Official auto instrumentation agent.
**Sergey** 18:58 Yeah. But…
**Pawel Filipczak** 19:00 What about, but what about the order, Sergeis showed you, where…
**Sergey** 19:05 By the way, why do you think that the order should not be changed? Because the placement is kind of, like, weird, right? It's, like, in the middle, like, it doesn't allow you to set the defaults, because then it's too late, because maybe I'll… and then also that will not allow you to override the defaults at the end.
**Bob Strecansky** 19:21 So it does… this does feel strange to me, right? Like, you have a bunch of new definitions there, and you have a registry enabled, like, halfway through, so I'm wondering, who's on the blame for this? I'm curious to see who wrote this To begin with.
**Chris Lightfoot-Wild** 19:35 Yeah, I was thinking the same, is it like a regression, or is it an intentional behaviour change?
**Bob Strecansky** 19:39 That… that was my thought, too.
**Chris Lightfoot-Wild** 19:41 Yeah.
**Sergey** 19:41 Is it source, does it come from, SDK resource?
decay resource… factory.
Blame.
I'm gonna guess it's Brett. Brett works on this exclusively.
But, oh, look at this, look at this.
**Bob Strecansky** 20:03 Yeah, it looks like you're.
**Sergey** 20:04 Somebody changed his mind.
**Pawel Filipczak** 20:05 There was a pull request, rework priority. You can see on the left side, 3 weeks ago.
**Sergey** 20:11 Okay, so we just need to upgrade to the version that, that has that. Okay, so I guess problem solved itself, just by looking at… Okay, back to you guys.
**Bob Strecansky** 20:20 That's… Git Blame is one of my favorite, like, you did it, you did it!
Not in a guilty way, just in a, oh, okay, that's why it happened. So, anyway, yeah.
**Sergey** 20:33 I ordered it solved, not in version 2, but…
**Chris Lightfoot-Wild** 20:35 Has that already been tagged, then? Sorry, that version there.
**Sergey** 20:39 Let me reshare.
**Pawel Filipczak** 20:41 Why don't we just need to talk to…
**Sergey** 20:42 Are you saying if there is already a release that contains that change?
**Chris Lightfoot-Wild** 20:45 Yeah, it's as simple as, you know, just bump me back.
**Sergey** 20:47 Is there a simple way to find this out in GitHub? Like, let's say I have this, so I can see which, Which, How do you… yeah, this is the commit that did it. How can I find out what was the nearest tag that contained this commit?
**Bob Strecansky** 21:04 That's a good question. I don't know that there is a good one of the… good way to handle that. I think that what I usually do is I'll copy that commit and go to the root of the repo and look at the releases and see if I can see that SHA in one of the… so, like, if you go to, just the root of this repo…
**Sergey** 21:21 commit, and then I go to the route, okay.
**Bob Strecansky** 21:24 Yeah.
**Sergey** 21:25 And then?
**Bob Strecansky** 21:25 And then, if you look at the releases on… oh, these releases…
**Sergey** 21:28 releases, yeah.
**Bob Strecansky** 21:29 These aren't moved, yeah.
Those are… it's, well, those go to, Yeah, that gets released with the Git split thing, so you have to go to that, read-only repository in, that first link, yeah.
**Sergey** 21:44 This one?
**Bob Strecansky** 21:45 Yeah.
**Sergey** 21:46 You mean the SDK one?
**Bob Strecansky** 21:49 Yeah.
**Sergey** 21:50 Okay.
**Bob Strecansky** 21:51 Whatever.
**Sergey** 21:52 You can search committer, like, okay, this is the…
**Bob Strecansky** 21:56 It looks like that 1.9.0… Probably has… you can look…
**Sergey** 22:01 How do you, how do you…
**Chris Lightfoot-Wild** 22:02 Oh, that reworked service batteries at the top.
**Bob Strecansky** 22:05 There's… there's that compare thing. I think that you could probably do that, like, you could compare to… it's… there's no easy way to find a commit in a release that I'm aware of, but…
**Sergey** 22:14 So they usually do it kind of, like, a really old-fashioned way, so I guess, probably… Yeah.
just go here, and I just start searching tags that contain this line that I want, so I will just…
**Bob Strecansky** 22:25 Yeah, that's kind of…
**Sergey** 22:26 the latest one, and then I will take one until I do, yeah, kind of, like, binary search. Okay, I see. I wanted to see if there's an easier way to do it. Okay.
**Bob Strecansky** 22:37 I wish there was, that seems like a good GitHub feature request.
**Sergey** 22:41 Okay. Okay, so back to… so I will find out, I will… I will find out if there's a tag that contains it.
**Bob Strecansky** 22:50 Awesome.
**Sergey** 22:51 Okay, back to you guys.
**Bob Strecansky** 22:56 Alright, Chris.
**Chris Lightfoot-Wild** 22:58 I don't know if you want to share your screen again, Bob, because the question… Sure. We're just following up from what we discussed last week.
Is that something that you already had as, like, you know, historical knowledge, that we just didn't know how to answer? Or… Is there… do we discuss this in, like, some sort of Slack thread?
**Bob Strecansky** 23:17 Are you talking… which one are you talking about? The FCC 2?
**Chris Lightfoot-Wild** 23:20 Yeah, last week's agenda was just, sort of, stuck the question on there about V2, and then some of the things were just sort of thrown out in the air, like…
**Bob Strecansky** 23:26 Yeah, I think… I think I don't… Brett has… I think he has an intent for V2 in his brain. I don't think he's ever eloquently expressed that to me, so I don't really have a strong opinion about how we're doing that. I think that that is definitely worth discussing in a Slack thread with him, because I think he has the most context for V2.
So.
**Chris Lightfoot-Wild** 23:48 it was around, like, how we've got one monorepo now, and we're doing, like, the Git split, and I think you said in the past it used to be separate, and then you pulled it together, and… But it was a… strong… I guess, reason for that, is that just because other SIGs do that, or…
**Bob Strecansky** 24:06 It's not because of the… it's not because other SIGs do it. The reason that… the Git split was originally created and is used the way that it does is because of the way that Symphony packages… or, sorry, not Symphony, Composer package, like, packages individual packages, and that was how, one of our previous committers, Tydall, used to… he wanted to make sure that we could, like, publish individual pieces of the API and the SDK as packages, and… That's, like, how it came about, and that's why it's living the way that it does.
**Sergey** 24:37 Yeah, originally the question was why we have more than just API and SDK, right, Chris? Like, it sounds like… because it was… it was, caused by the question, okay, what will happen to other packages if we have V2 of SDK? Will some of them also will have to have.
**Chris Lightfoot-Wild** 24:51 V2, I assume API will not have V2.
**Sergey** 24:53 But others made.
**Chris Lightfoot-Wild** 24:55 Yeah, some of the other complexities around, like the context and, SEMCOM and… I mean, SEMCOM makes, I guess, sense in itself, but then even on the contrib side.
There's obviously a whole bunch of unrelated packages that are, like, split off from each other.
And then, just, it's difficult, obviously, looking at the tags that we've just seen.
Between different repos, because the commits and the shares are all different.
And, like… I agree. There's some headache around the whole thing, just, like, and it seems arbitrary that we've… I don't know.
**Bob Strecansky** 25:27 Yeah, I think… I agree with you. I think it's a difficult problem that we've backed ourselves into, and we have to come up with a plan of how to tackle it. I don't have a good answer.
**Chris Lightfoot-Wild** 25:35 Cool. So, is it worth starting a, do you think, discussion thread in Slack with… and see what Brett thinks about it? Obviously, we don't…
**Bob Strecansky** 25:42 Yeah, I think…
**Chris Lightfoot-Wild** 25:43 Don't know when he might next be around, so…
**Bob Strecansky** 25:45 Yeah, I think… he's been, like, working behind the scenes, I think. Like, he's definitely been reviewing PRs and doing stuff, so I think that he'll respond, but let's just be conscientious of his paternity leave, and…
**Chris Lightfoot-Wild** 25:57 Yeah, my pleasure.
**Bob Strecansky** 25:58 We don't need to release this today or tomorrow or next week, so… I think it's starting a thread there.
**Chris Lightfoot-Wild** 26:05 I think there's no rush on it, it was.
**Bob Strecansky** 26:06 Yeah. Yeah, I think in the open… in the public channel, it's good, too, so that we can get input from the community if anybody else has anything that they want to say around that, because this is definitely a PHP-specific thing, but… Is, like, is… Busy enough that we can probably garner some good feedback from others, too.
**Chris Lightfoot-Wild** 26:27 Cool, thank you. I don't mind starting a thread then, if…
**Bob Strecansky** 26:31 Brookly with that?
Yeah.
**Chris Lightfoot-Wild** 26:34 Thank you.
**Bob Strecansky** 26:35 Thank you for, championing… championing… championing that. It's a… it's something that I think we have all been thinking about in the back of our brain, but I'm glad that you brought it to the forefront. I appreciate that.
**Chris Lightfoot-Wild** 26:49 Well, it was predominantly Sergey, I think, speak with most of those questions, so, yeah, thank you, Sergey.
**Bob Strecansky** 26:54 Thank you, Sergey. Thank you, Chris. Thank you, pal.
**Sergey** 26:57 Thank you, guys.
**Bob Strecansky** 26:59 Alright, we'll see you all on the internet.
**Chris Lightfoot-Wild** 27:01 Drizzle.
**Sergey** 27:02 Bye.
