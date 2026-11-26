SIG: JavaScript SIG
Date: 2026-11-25
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Marc Pichler (Dynatrace)** 00:13 Hello?
**Trent Mick** 00:26 you know…
**Jared Freeze** 00:43 I'm just listening in. I always keep notes. And I worked in the hospital.
**Marc Pichler (Dynatrace)** 00:49 I'm gonna share my screen real quick, then we can get started.
Alright.
So… So, the first topic here is something that I added… I saw this question pop up, it kind of originated from OpenTelemetry Lambda, where they have currently migrated to the Node SDK thing they had previously done, their setup, kind of… themselves, somehow.
And one thing that they ran into there is that they need to manually deregister stuff for their test, and… are now asking for something that would undo exactly what Node SDK start did, so also unregistering it from the API, in addition to the shutdown, probably.
I did go digging into the spec and, was trying to figure out whether unregistering an SDK from the API is even, Thing that's specified, and it's not.
Java, for example, has, method, regardless, to, Remove anything that's registered for testing purposes, but we don't have anything like that.
It's fairly simple, though, to unregister these things.
Because one can just go through the list of things that are exported by the API and just call disable on each of them.
One of the other use cases for this that came up here was SDK reconfiguration, but I think that's something that we want to support explicitly in the SDKs themselves, rather than providing a workaround where people Unregister, obtain new traces and meters, and generate their new instruments and whatever, and then, like, continue as if nothing happened.
After that, I think that's a bit of an ugly workaround.
Not sure what your opinions are on this.
**Trent Mick** 03:29 I strongly agree with you.
The only case that's driving this is for testing, and that's the tail wagging the dog here. We do not need to complicate the runtime code for this at all. I think maybe we could add better docs for… new Node SDK, or, like, don't even bother, because we want to move to start Node SDK. I'm saying that, like, this intentionally does register with global providers. If you want to undo that, then that… because for the reason that you gave, that someone else may have come in and disabled and registered at different global providers, so undo isn't… something that can be cleanly done by the thing 100% reliably, so it's really on the caller to do that, and just show the example code how to do that. And that's just… yeah, I mean, you know how to do it. You just call .disable on the global provider.
Thanks. So yeah, I strongly agree with you on that one.
Also, I guess… If I have time, I'll follow up.
So Thompson… Tomo, I gather, is the maintainer of the Lambda stuff, or maybe just the Node.js Lambda side, I'm not exactly sure how the maintenance. There was someone else that was involved, like, a couple years ago that had intentionally set up the Lambda Node.js bootstrap stuff to… I think at the time, at least not use auto instrumentation's note. The main reason was he was trying to get the cold start back Time down, and so he had that… got that thing bundling, and probably that's when they moved away from using Yeah, I don't know if at any time they were using SDK Node.
I could see Thompson's argument for wanting to do that, so they don't have to maintain changes and things going on there, but I guess the timing's a bit unfortunate.
**Marc Pichler (Dynatrace)** 05:18 Yeah, I think, migrating to start node SDK should be… Fairly okay, to do.
from what I've seen, the way that they use it,
**Trent Mick** 05:33 Yeah, if they're not exposing the options, then it should be a straightforward change, yeah.
**Marc Pichler (Dynatrace)** 05:37 So… I'm hoping that will go over smoothly.
one of the reasons why they weren't using it before was also because we were doing some weird things in, Node SDK, like, lazy requiring the Jager exporter.
And… Other things that would have caused trouble.
Also, I think the auto instrumentation node wasn't included, because back then we also had a Quite the slowdown, on startup when, the require in the middle.
**Trent Mick** 06:18 Right.
**Marc Pichler (Dynatrace)** 06:18 thing was running, because I think it would just stack stuff on top of each other, so the more instrumentations you had, the longer it would take to start up.
Up to minutes at some point.
So…
**Trent Mick** 06:32 that before the singleton? Like, I wonder if some of that slowness still exists, to be honest, but I don't know.
**Marc Pichler (Dynatrace)** 06:38 Yeah, I think, like, it's still slower than not having any instrumentation, I think, but it's way better than what it was.
**Trent Mick** 06:48 Okay.
**Marc Pichler (Dynatrace)** 06:49 So I think all of that together might have been enough for them to now switch to… No, that's okay.
But we'll see if… Any problems pop up there.
**Trent Mick** 07:05 So yeah, I agree with you on that one, I can… If it helps, I can add a comment to the thread there, too, to give a second opinion.
**Marc Pichler (Dynatrace)** 07:15 I will, I'll just summarize what we talked about after the meeting and write a comment there.
And I might reach out to you, in case I need some backup.
**Trent Mick** 07:26 Okay, sure.
**Marc Pichler (Dynatrace)** 07:27 Thanks.
Does anybody have anything else you would like to talk about?
On this topic right here.
If not, then I guess we can move on to the next one, which is Modelio.
**Marylia Gutierrez** 07:48 Yeah, and thanks, Trent, for allowing me to keep ahead. Yeah, of course. Yeah, so, yeah, basically, like, just a few FYIs. So, we are doing Auto Unplug, again. I don't know if anyone here attended, the one that we had this year, but we are doing it again, next year in February, so registration are up.
It's in a conference, so pretty much how it works with, like, bring the topic, so that was, like.
a pretty nice way to have… also, we had a bunch of end users there as well, it was pretty nice, but just a chance to talk with other maintainers and things like that. So, yeah, just sharing here, people want to attend, I think it's… it was definitely worth it.
**Trent Mick** 08:26 I've been checking, but I haven't seen my plane tickets in the mail yet.
**Marylia Gutierrez** 08:32 Yeah, we are definitely sending to all maintainers, yes, it's true.
**Trent Mick** 08:36 Yeah.
**Marylia Gutierrez** 08:41 Yeah, we are using the same space we did last year. It was a pretty cool venue that has, like, one floor, so we can decide the topics, and then the other floor with, like, a bunch of rooms, so we can divide the people on the topics.
Cool. The other topics, also just an FYI, we are doing, again.
brand, like, break at the end of the year, so all meetings should be canceled the last two weeks, of December. We probably can put something like, yes, like a note on the… on the… our notes, put, like, no meeting here, just in case someone shows up and are kind of, like, lost, because we're probably not gonna delete on LFX, just because it's a little annoying thing there. But yeah, just another FYI. And third one… so there is a topic that came up. We are just… basically trying to see people, how they feel about it. So we are trying to get more people from Asia countries to contribute, and a lot of, like, sometimes the feedback is, like, it's hard for them to attend meetings, and people will like to see more things being discussed async.
So one way of doing this is kind of, like, forcing the meetings to be very, like, concise and very, like.
we really need to discuss this topic in person, so yeah, should focus like this, but then try to bring the majority of topics async on Slack.
Also help with, like, language barrier, because then people can read or use, like, tools to translate and things like that. So, apparently, like, a few SIGs already changed to 30 minutes and has been working, so we are trying to just bring this topic to other SIGs to see how people feel about it. So, nothing is, like.
mandatory or anything like that, but just as, like, a tryout basis, in case people have any strong opinions, but yeah, just bring in the topic.
**Marc Pichler (Dynatrace)** 10:41 I think often we… would call it a meeting after 30 minutes anyway, so… I'd be okay with shortening a bit.
Not sure if anybody else has opinions on the topic.
**Trent Mick** 11:01 Yeah, we do tend to be short, though we do, sometimes go over 30 minutes, so I mean, I don't know.
I have a strong opinion.
This is also, you know, one of my weekly support groups, so… They're asking a lot, really. I was gonna say…
**Jared Freeze** 11:18 SIG. Not my main SIG, but I feel like there is a lot of async already. Like, there's a lot of activity on PRs in this group. Like, browser, for instance, like, we get quite a lot done on video.
But I feel like this one has way more volume, and… I don't know. I feel like I'm reading a lot.
Just my two cents.
**Marylia Gutierrez** 11:40 Yeah, we can probably, like, at least for a while, try to keep, like… we keep as the one hour and see how we feel, like, cutting on the half hour. I don't know.
But yeah, I feel like this is a good SIG, as you all mentioned, but in case you have other SIGs, also try to bring this up to other SIGs.
**Marc Pichler (Dynatrace)** 12:00 I will, have a look at the, Excel.
Sheet that we have with the meeting links, and see how long they… ran the last few times, to get a better feel of, like, how much time we usually need.
But yeah, we can definitely revisit, the topic.
In the next few weeks and see.
What we feel comfortable doing there.
**Trent Mick** 12:28 Now that you say that, I feel like I've been able to verbal diarrhea almost to the end to avoid the triage section.
So… Anyway.
**Marc Pichler (Dynatrace)** 12:44 It doesn't.
**Trent Mick** 12:45 Speaking of, it's now me with two long topics.
**Marylia Gutierrez** 12:50 No way.
You're sorry, no, too much.
**Trent Mick** 12:55 Alright, so, okay, I've been trying to get declarative config over the line, and I feel the next… the last couple of steps there, at least to get a release out where people… we can bless it, is… One of the final ones is this first bullet point, is documenting StartNode SDK and promoting that in the README and SDK nodes, so that's kind of the first public time that we say, hey.
start considering this new thing, and eventually, but not yet, we'll deprecate New Node SDK.
For the new one. So I've been documenting that. So yeah, the question here, and I think maybe Mark answered it already, is do we feel the need to have all of the options to start Node SK documented in the README?
As opposed to just pointing to either the API docs, or I had… currently, I just had links to the… To the types file in GitHub, but I'm not sure if that's… Appropriate. The reason I don't necessarily want to do that is because with the start node SDK options, I've… there are doc comments that, you know, show up in autocomplete in an IDE for all of the options that do an okay job of documenting. The only thing that I would do in the README is at least in my preferences, document the interesting ones that could use more space for pros, so showing example usages, or talking about nuances with environment variables that impact them, stuff like that.
So… welcome thoughts on that. It'll mean I'm removing… Docs that are already there.
**Marc Pichler (Dynatrace)** 14:28 I think I'm fine with, keeping it lightweight there.
And just linking to the API docs. I would prefer the link to the API docs over… Linking to the actual types.
Okay.
mainly…
**Trent Mick** 14:46 Q.
**Marc Pichler (Dynatrace)** 14:48 we… Like, the way that we would link it would be, Like, we would have to link into the built… directory, somehow, for people that actually pull the package to get access to it, or we would have to put a permalink there to GitHub.
Which might require us to change it all the time when we release.
**Trent Mick** 15:15 So, okay.
one boo on GitHub for not allowing me to do a search into a file.
for… like, because, like, a year or so ago, they added that sidebar on when you're browsing code, that it knows about symbols in the thing, right? So I just… I want to link to a particular symbol, and it can jump to the thing. I realize that's potentially a hard problem. But I had been linking to just a search within a Google search within the repo that shows the HIS for that. So yeah, maybe the API docs are better.
To test my understanding, I need to do a… An update.
that exports that type before it'll show up in the API docs, is that right?
**Marc Pichler (Dynatrace)** 16:01 Yes. I think the way that it works is it just shows anything that's in one of the entry points.
And… multiple entry points, we also have to configure that in TypeDoc to make sure that it shows up.
**Trent Mick** 16:17 Okay, I'll work on that then.
Thanks.
Sure. Okay, second bullet point is, I think, the declarative config, from my point of view, there are three things to look at. One is that first PR for custom component providers, but I just saw as I was writing this that, Marc, you've given me some review on that, so I'll go take a look at those review points.
The second one is a new PR for me, adding an option called Customize Config, which is following on a functionality that OTel Java has, and I try to give most of the pros there as giving justification for why we'd add this. So, it's an option that you pass to Start Node SDK that… with a function that the caller can use to post-process the parsed YAML file, so the configuration model.
to add what limited things it… or make modifications it might need for that, for its distro before passing on. The class… or before then… Start node SDK does the, create step to create all the SDK components from that config.
Generally, this isn't a mechanism that should be used, because the idea with declarative config is the WYSIWYG is what you see is what you get, so it should all be explicit. But the classic example, which, the Java agent, Hotel Java Agent uses itself, is to add a resource detector for the telemetry.distro resource attributes. So, you're providing a distro for users to start their SDK, and semantic convention says you should set the telemetry.distro things, but you don't want to have to have the users add those fields or that resource detector to their config file, so this would automatically add that resource detector.
To the end of the list, and then move on. So… That was the argument for that.
**Marc Pichler (Dynatrace)** 18:16 One of the things that I'm… That kind of sticks out to me is, It looks like this customized config wouldn't be needed if we had create exported, right?
Because if we have create exported, then… One could parse the config model, which is a one-liner, and then change it, and then pass it into… Create.
**Trent Mick** 18:50 Yeah, there's a little bit… there's a little bit more going on in Start Node SDK, or from.
**Marc Pichler (Dynatrace)** 18:58 confused.
**Trent Mick** 18:59 But you're right, there's not a whole lot more. There's constructing the shutdown function, there's making sure you get the order right, there's calling register instrumentations at the right time, that kind of thing, so… Yeah, there's a little bit more going on, but you're right, if we expose the base components there, then SDKs can put it together themselves.
Yeah.
the… a couple of things that I point to, it would clarify a thing in… I noticed when Matt Ware was doing the… config provider stuff, so instrumentations can get their config. I noticed in Dasho's PRs he pointed to, they have another PR where they're trying to use StartNode SDK in their distro, and they're adding hacks. They're doing monkey patching of start… of parts of… SDK node, or parts of one of the other things to add the resource detector for doing exactly this.
I know Elastic's own distro for OTEL Java is using that customized config for the exact same purpose, for adding a telemetry.distro, so it seemed reasonable to add this, but… Feedback walking.
**Marc Pichler (Dynatrace)** 20:06 I'll have a look at, And I will see, if I can… Find another way of doing it.
I'm not sure if the, like, any way that I can come up with would be… better than this, probably not, but I'll give it a shot and see if… There's other ways to accomplish this, too.
**Trent Mick** 20:34 Okay.
**Marc Pichler (Dynatrace)** 20:35 I'm not completely opposed to actually doing it, like… You, showed it here, I think it is.
Looks… looks reasonable.
So… Sounds good.
**Trent Mick** 20:49 Okay. So if we got those in, then I'd want to do… or maybe… if it's going to take a while, maybe we do a release of HotelJS before those things go in? I mean… It's a bit easier if those go in first and we do that. There are a bunch of other… there's some other, changes… In the repo that I think would be good to release.
I think especially that one from Raphael that fixed all the warnings about undefined resource attributes.
And we get a bunch of Diagorns right now, so it'd be nice to clean those up.
**Marc Pichler (Dynatrace)** 21:19 Intentionally not released anything, because we didn't have any high priority.
Bug fixes that needed to go out.
I wanted to avoid deeper.
Getting surprised before.
Black Friday, so… maybe if we can wait until next week, or…
**Trent Mick** 21:40 That's Okay, maybe we try to get these things decided first, and then we can do a release next week, that's cool.
**Marc Pichler (Dynatrace)** 21:48 Sounds good.
**Trent Mick** 21:51 I hope people have turned off, if they care about Black Friday, have turned off auto…
**Marc Pichler (Dynatrace)** 21:56 Yeah, one would hope.
**Trent Mick** 21:59 it didn't deployed.
Okay, yeah.
**Jared Freeze** 22:03 I mean, does anyone really use the auto-merge from Renovate?
It seems wildly dangerous.
**Marc Pichler (Dynatrace)** 22:11 So, I do use it, but also… I have to cut a release manually for the components that I own, so…
**Jared Freeze** 22:23 I sure hope so, yeah. The CD part, I mean, we all do CI, but I don't know anyone that does CD.
**Trent Mick** 22:28 A CD, that's crazy, yeah.
**Marc Pichler (Dynatrace)** 22:37 Aye.
Any other topics we should discuss?
Or anything that… Still goes into one of the existing topics here.
**Jared Freeze** 22:47 I just have a quick update, which is that we had a couple PRs that add, TypeScript hint for deprecated for browser, and they link to… Browser repo.
they are not the same, so the… what Martin suggested was to add guidance that… The instrumentation name?
Has changed, so if you're doing filtering, you need to update, or whatever.
the data model's also different. It kind of just says, like.
go look at the browser repo and read the new docs. I feel like that's sufficient. I know tons of people are still using every… everything in the repo, fetch in XHR, specifically.
Including my company, so I feel like we just gotta, you know, rip the band-aid off, though. So, the hints are going in. As far as calling NPM deprecate.
to, like, really, like, you get the install warning, you know, and if you're doing a strict NPM install, it literally won't do it.
I'm gonna put that off as long as possible. I feel like we should wait, you know, maybe even for the next major, just, like, let it sit there for a while. Because most people don't have strict TypeScript.
Compilation or checking on.
But you will get, you know, red underlines, which was kind of the point, you know, to sort of nudge people, or whatever. But, yeah, just want to let you know, I merged one 5 minutes before this meeting, and there's another one It's just waiting on some changes. So… if… you're gonna do a release, please just post in Slack, and I'll try to expedite that one. Or maybe… actually, David's here, maybe David could just check it out.
Oh, no, never mind. It's blocked by Martin. I think Martin has to undo his request changes.
But… Yeah, that's why I came, just to ask if there's an imminent release.
**Marc Pichler (Dynatrace)** 24:41 Yeah, there's, I think we will go ahead with it next week, unless there's anything, super pressing that comes up.
We want to release.
To speak over to.
**Jared Freeze** 24:54 Okay, yeah, and I mean, you're absolutely right. Black Friday is… Is a big one.
**Trent Mick** 25:03 Where's your PR? Just so I know exactly what we're talking about.
**Jared Freeze** 25:06 It's called…
**Trent Mick** 25:10 And it did merge, or not yet?
**Jared Freeze** 25:12 I merged one, not the other, so… It's a 3832.
The one that merged was… 3927.
**Trent Mick** 25:29 That's true.
**Jared Freeze** 25:38 Yeah, sorry, Kintrib.
**Trent Mick** 25:41 Okay, so not yet, like, fetch and ex-signature, which are… Have more visibility.
**Jared Freeze** 25:49 Yep.
**Trent Mick** 25:49 I swear, I think it's probably a coincidence with, like, the AI age, but when we, like, started saying, okay, browser… is… got their all instrumentations. The number of PRs that were coming in for instrumentation fetch and NextHR of… have jumped. Like, there are a lot sitting open, and I don't really know… I mean, I don't have enough time to get to all the… PRs and issues as it is. The browser ones, I basically just punt, I don't know what we want to do there.
**Jared Freeze** 26:15 No, that's fine, and I saw that JS approvers is sort of lagging, which is good and fine. I mean, at this point, we need to… you know, we just talked about this on Slack in the… browser that, you know, what I really want to say is.
Hey, we're frozen, which was part of the deprecation notice.
I think we're gonna have to keep responding to people, because these PRs don't seem code-aware, to be kind.
They're just flybys, and so… What I've gotten in the habit of doing, I haven't done it in Contrib yet, but is just saying, hey, where did you see this?
And typically, the answer is, oh, well, Claude…
**Trent Mick** 26:55 Yeah, yeah, fear.
**Jared Freeze** 26:55 theoretically, has found a bug. And I'm like, that's fine.
no one wants a bug, but, like, show me. Like, give me an example, give me something. Give me a test. And so…
**Trent Mick** 27:07 Yep, I totally agree on that one. Yeah, that number that come up where it's… yeah, we don't have a… I just… I found a theoretical thing, not an actual something.
**Jared Freeze** 27:17 Yeah, actually, David made a good point, which was, like, I built in this, really overbearing protection scheme for, like, integrity. Like, if you have bad instrumentation, I was checking for, like, enable and disable, and, like, is it an object, and is it not null, and blah blah blah blah.
And I think it was your comment, that was just like.
you know, check for enable, disable, call it good. Like, if people pass something terrible, like, they'll figure it out.
Like, we don't need a handhold for absolutely everything, and I was like, okay, good enough for me.
You know, because you can only do so much, so…
**Trent Mick** 27:51 Yep.
**Marc Pichler (Dynatrace)** 27:54 Especially…
**Trent Mick** 27:54 Is it Rust, man.
**Marc Pichler (Dynatrace)** 27:58 I've seen a lot of PRs recently come up where it's very clear that this probably hasn't happened anywhere in production, and in some cases isn't even reachable the way that the code is written.
So,
**Jared Freeze** 28:15 A lot of times, too, we have conflicts, like.
they'll use a feature that's not baseline widely available, but then say, this happens in Android 6, And it's like Android 6 won't.
**Trent Mick** 28:26 Beautiful.
**Jared Freeze** 28:27 and execute.
**Trent Mick** 28:27 It doesn't implement the thing, so yeah.
**Jared Freeze** 28:29 Yeah, so, yes, that is an edge case that, you know, maybe you can get there if you compile down to ES2012, or whatever, you know.
So… Yeah, good luck.
**Trent Mick** 28:42 Yeah.
Okay, cool.
Sounds great if those are ready to be deprecated.
And… Guess we're not clear, frozen.
But if no one's looking at the PRs, then they're effectively frozen, so…
**Jared Freeze** 29:00 Yeah, and like I said, something… you know, if there's security, of course, I would take a security patch, but, you know, just kind of, like, edgy stuff, I'm like, I don't want to waste time, let's focus on browser.
**Trent Mick** 29:13 Yep. Cool.
Thanks.
**Marc Pichler (Dynatrace)** 29:20 So, we're now right at 30 minutes,
**Trent Mick** 29:25 Really, you lefto.
**Marc Pichler (Dynatrace)** 29:30 Huh, yeah. Anyway, anybody opposed to calling this a meeting?
**Jared Freeze** 29:38 I know Trent's not, as we're just arriving to untriaged.
**Trent Mick** 29:43 I do feel like the guilt is… guilt is getting me… no, I don't want to do the triage, no, but guilt is getting me, because I see Jackson down there at the bottom. Jackson, I swear I'm still looking at that PR, but I just… anyway, I'll get it.
**Jackson Weber** 29:56 I…
**Trent Mick** 29:56 If you're like, any part of your life or professional life is being held up because I'm not merging that PR, then let me know.
**Jackson Weber** 30:04 No, the worst of it is just that my open PRs list is one PR longer. And, yeah, you know, I'm sure we all have lots of open PRs, so it's okay.
Oh, but I appreciate it. Thank you, Trent.
**Trent Mick** 30:27 Okay, 10.31, we went one minute over.
The new soft deprecation limit for medium lengths.
I'll shut up now. Muter.
**Marc Pichler (Dynatrace)** 30:42 Then, I guess we can end the meeting here. Thank you, everybody, for joining. Thanks for the discussion. Have a nice week, and see you next week.
**Jared Freeze** 30:54 Alright.
**Jackson Weber** 30:55 Have a good one, y'all. Bye.
**Marc Pichler (Dynatrace)** 30:57 Soon.
