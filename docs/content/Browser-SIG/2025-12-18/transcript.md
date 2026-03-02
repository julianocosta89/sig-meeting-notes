SIG: Browser SIG
Date: 2025-12-18
Duration: 33 minutes
Zoom Recording URL: https://zoom.us/rec/share/PTVlVqTdfs8issYzwYSPvkj1l3q6c0EXxNXNV1bAR48uefY3fuEufLOi2bFPNfV6._fPZVwrXC3qnU5MU
============================================================

## Zoom Recording Transcript

**Jared Freeze** 01:00 Hey, what's up?
**Martin Kuba** 01:02 Hi, Jared.
**Joaquín Díaz** 01:04 Nope.
**Martin Kuba** 01:07 Hey, Joaquane, how are you doing?
**Joaquín Díaz** 01:09 It's amazing.
**Martin Kuba** 01:12 I done.
I think Ted should be able to join today, so…
**Daniel Dyla (Dynatrace)** 02:01 I think this is likely the last week of productive meetings for a lot of people.
**Martin Kuba** 02:06 Yeah.
And this, next two Thursdays… next two Thursdays fall on holidays, so… I think this…
Meeting's not gonna happen, next meeting's not gonna happen until, like, January.
So, whatever.
**Jared Freeze** 02:29 That'll give people plenty of time to do reviews.
**Martin Kuba** 02:33 Yeah.
Yep.
**Jared Freeze** 02:37 I've been hammering the quarter repo with just all sorts of things, so…
Getting to know everybody over there, including Trent.
Fair enough.
**Daniel Dyla (Dynatrace)** 02:47 I've been… Some would say suspiciously absent from the core repo recently.
Probably. Including Trent.
**Trent Mick** 02:55 Yeah, dude.
Where are you?
**Daniel Dyla (Dynatrace)** 03:01 I, I've been… Going through a job change internally.
**Trent Mick** 03:07 Mark mentioned you're enjoying it, so…
**Daniel Dyla (Dynatrace)** 03:10 Yeah.
**Trent Mick** 03:10 Let's kid.
**Daniel Dyla (Dynatrace)** 03:11 To be determined what it means, like, long-term. I should have a better idea in January.
**Trent Mick** 03:17 I'm transitioning to be a lawyer.
Because Jared asks me copyright assignment questions on things, so…
**Daniel Dyla (Dynatrace)** 03:25 I did my stint as a lawyer.
on the GEC.
**Trent Mick** 03:30 Nice. Yeah, never. I'm never gonna apply for the GC.
**Daniel Dyla (Dynatrace)** 03:42 I don't see anything on… oh, no, we do.
PR reviews, yeah.
Not much on the agenda today.
**Jared Freeze** 03:53 I mean, there's definitely things I want to go over, but they belong written down, and…
like, commented. I think it's, like, things we have to think through, but,
I would really like to use the package,
the packager thing that I posted last week, I think it's pretty useful. It does give repo access to just…
You know, this company, so…
I'll make an issue for it, though, so we can leave it, because I think it's…
incredibly useful for cross-repo stuff. You know, I think it'll help a lot.
We'll see.
**Trent Mick** 04:32 I'm not sure I totally groked what that was gonna help with.
**Jared Freeze** 04:37 It lets you… so, like, in a GitHub action, it'll let us, properly, like, package install from main, or next, or whatever we want in other repos, right? So, it'll… every commit on main will actually become, like, a proper package, like, unreleased.
but available to install in a normal way. So literally, like, npm install core repo at… Commit ID?
That's what that does. So, under the hood, it's really just npm pack, and then pushing to Cloudflare.
But I think it's pretty cool, because that means we can make integration tests that do things like
here's the test that a new PR in the browser repo runs against hotel main, runs against hotel release, you know, runs against maybe some other thing that I've chosen.
**Daniel Dyla (Dynatrace)** 05:27 That's awesome. We should do that in the contrib repo, too.
**Jared Freeze** 05:31 Yeah, it does.
**Trent Mick** 05:31 this before, but this is something that people would have told me to use for Dacio before, is that right?
to create, like, a local npm repo setup, and manually do your publish to that thing, and then test against doing that. Yeah, okay.
**Daniel Dyla (Dynatrace)** 05:45 Yeah, that's local, though. It sounds like what Jared's talking about is,
Actually pushing to a cloud service.
**Trent Mick** 06:01 if we just dropped this whole TypeScript thing with build steps and stuff like that, and just had…
you know, because who wants types? Then we could just author it in JavaScript, then we could just use the npm and install directly from the Git.
commit, right?
**Jared Freeze** 06:16 I mean, Node does typespex.
**Trent Mick** 06:18 Let's move on.
Sort of.
Sort of. It intentionally disallows importing, doing,
importing TypeScript code if it's under a node modules folder. Don't actually know the reasoning behind that. I think it's because they're like, whoa, let's put the brakes on this whole…
**Daniel Dyla (Dynatrace)** 06:38 Yeah.
**Trent Mick** 06:39 thing, but yeah. Anyway.
**Daniel Dyla (Dynatrace)** 06:42 But also.
**Trent Mick** 06:44 Sure thing.
**Daniel Dyla (Dynatrace)** 06:45 We're talking about testing, and the only thing it broke in the core repo was tests.
**Trent Mick** 06:52 For Node, you mean, or for hotel?
**Daniel Dyla (Dynatrace)** 06:55 Yeah, the node type stripping.
**Trent Mick** 06:58 Yeah, yeah.
Which, we're still kind of living in a… we haven't solved that, I think, are we? We still have the disabled type.
**Daniel Dyla (Dynatrace)** 07:07 Think so, yeah.
**Trent Mick** 07:08 Yep.
**Daniel Dyla (Dynatrace)** 07:14 I don't see anything else on the agenda, so I guess I can,
just raise a topic that came up during the spec call. I wasn't planning on bringing it up, so I don't have anything prepared, but,
They talked about… Changing the exporters to do some level of either feature detection or… In…
the case that would be more interesting for this group, I think, protocol negotiation.
I know that exporters and export protocols have been a pain in JS for a long time, and more of a pain in the browser than they are in the rest of the JS world.
Obviously, to do protocol negotiation, you would need to support multiple protocols on the client, which inflates your size a little bit, but it would mean, potentially, if you have something that only supports JSON, for example, and you want to
Dump the, Protobuf dependencies, or whatever your…
server, backend, collector, whatever, could detect that you're sending JSON, and then it alleviates some configuration headaches that we have.
I don't know about you guys, but I hear all the time about
people who have misconfigured and are sending JSON to a protobuf endpoint.
**Ted Young** 08:46 I mean, I feel like… short run…
We probably just, like, pick a configuration.
Right, like, I feel like long run, we were probably planning on the… whatever we're shipping to the browser to be, like, more specialized than what's in Node, and maybe locked
locked down a bit on that front, but I don't know.
That was kind of a presumption we were making based on presuming we would get more efficiency and smaller package sizes out of
tackling the SDK is, like, part two.
**Daniel Dyla (Dynatrace)** 09:24 Yeah.
**Jared Freeze** 09:24 I think there's a big difference between the package size and, like, stuff going over the wire.
And that G-Zip over the wire matters way more than the package size. I know it's what everyone obsesses over out of the gate, because they're like, oh, I already have an app, I don't want to add 50K. You're like, great, but you also don't want to save 50K of JSON, right?
Or whatever. So,
I don't know, I think that compression's pretty essential. I don't know if you're suggesting, like, just straight… text
I don't know, I find the binary one up so much smaller.
I'm not sure if I'm off-base there, but…
**Ted Young** 10:03 I just meant more around, like, having some kind of, like, negotiation and flexibility. Sounds like a feature.
you know, we don't necessarily need to ship… keep shipping to the browser in a long run, right? It could be hardwired to be protobuf or hardwired to be JSON, but…
Like, oopsie, we might have, like, a misconfiguration between, like, what the browser is sending and, like, what the endpoint is expecting, is maybe… like, we're gonna be in a scenario where it's like, hey, if you're shipping this thing, always use this, like, publicly facing gateway thing that we recommend.
We could probably, like… Not have to do…
that negotiation, it could probably just be hardwired. That's all I was saying.
Or at least, if I understood what you were saying, Daniel, right, is, like, people want to add some complexity to the exporters to deal with protocol negotiation, and that was going to inflate the side… size of the package.
**Daniel Dyla (Dynatrace)** 11:06 No, I guess I was saying more… I was not suggesting that the client would support multiple protocols, because…
I don't… I just don't think that's needed. What I was saying is that…
if the mechanism… and like I said, I wasn't even planning on bringing it up here, but there is a potential world in which
The mechanism simplifies configuration and reduces the chance to misconfigure a collector when you're using it with
A browser exporter that only supports certain, you know… because…
if we choose a winner, you know, say Jason, I don't know if that's what it is for the browser, and we say this is the only thing we support.
And people…
are configuring their collectors, and they configure protobuf endpoints, there's a potential, like, mismatch there, you, you know, people don't know why it's not working or whatever, where instead, you could have… this is the OTLP receiver on the collector, you just turn it on, and it will figure out what you're sending and handle it appropriately.
**Ted Young** 12:12 Oh, okay. My bad.
You're talking about, on the collector's side, it being able to negotiate those things better.
**Daniel Dyla (Dynatrace)** 12:19 Yeah, the conversation, on Tuesday, was actually more about, like, feature negotiation than anything, but I think it, if the mechanism is general enough, it could also alleviate some configuration headaches for us.
**Trent Mick** 12:39 What's an example of a feature?
That would be negotiated.
**Daniel Dyla (Dynatrace)** 12:44 I don't remember what… which feature they were talking about on Tuesday, but I can pull it up, because it came up in relation to a specific…
**Ted Young** 12:59 Yeah.
**Jared Freeze** 13:09 I have a quick question. Is it more confusing to intend to use one
And accidentally use the other, and then it works, and you sort of never know.
**Daniel Dyla (Dynatrace)** 13:22 What do you mean?
**Jared Freeze** 13:25 Like, if JSON's working, but you intended to use…
like, not JSON, is that worse? If it just works out of the box, but it's not actually what you want.
**Daniel Dyla (Dynatrace)** 13:36 Well…
If the browser only supports one thing, like, if the browser exporter only supports one protocol, then that would always be the one we want them using anyway.
**Ted Young** 13:51 Yeah.
I see what you're saying, Jared, but I also think it's the kind of, like…
I think I would rather have them having it work by mistake, given that, as long as the data's getting there, it's just like, oh, it was a little more expensive than maybe you thought, or something.
You know what I mean? Like, if…
**Jared Freeze** 14:13 I just want to be… just wanna be careful that, like, it doesn't, you know, have a bad first impression of, like, oh, this thing's too big, I'm not gonna use it, so…
**Ted Young** 14:23 Yeah. But yes, heard.
Where I think this will actually be helpful, Daniel, is, like.
we're also looking at additional, newer protocols coming down the line, right? You know, there's, like, Apache Arrow, like, Otil Arrow. There's also Steph, which is, like, a really compressed metrics format that Tigrin's been working on. So I can totally see a future where we start rolling those things out, and maybe…
even having some, like, dynamic upgrading or something, but it would be… I could see it being nice in the long run for the collector.
**Daniel Dyla (Dynatrace)** 15:02 Yeah.
**Ted Young** 15:03 What's about?
**Daniel Dyla (Dynatrace)** 15:04 ink…
I think the Arrow Protocol stuff is actually where that content negotiation originally came up in the spec call.
which… Browser is unlikely to support in any near-term future.
**Ted Young** 15:22 Yeah.
Arrow's, like, the opposite of what we need.
Lake.
A stateful long-term protocol that's not good for short bursts of communication.
**Jared Freeze** 15:42 I was just gonna mention, we got our first, outside instrumentation submitted.
To catch pencils, so… I don't know if anybody saw that, yeah, so that's kinda nice.
I haven't approved it for workflow runs or anything like that. I wasn't sure, kind of, what the…
what the process is for that. I know that
I don't know if people can steal sequence and stuff like that. That's why it's turned off, right?
**Ted Young** 16:17 Wait, what's turned off?
**Jared Freeze** 16:19 Like, new members can't do workflow runs.
**Daniel Dyla (Dynatrace)** 16:25 Yeah, that's enabled by default on all… I think it's not even all OTEL repos, I think it's all CNCF repos.
It's so that people don't open up PRs that run Bitcoin miners.
**Jared Freeze** 16:41 Yeah. Cool. So what's the process for allowing that?
**Daniel Dyla (Dynatrace)** 16:47 You just click allow. Any maintainer can click allow.
You know, you look at it, it…
it doesn't take much more than a cursory examination, I think, to say, like, I don't think they're including anything totally… it's not meant for you to catch every tiny possible, like, supply chain bug, although ideally, you do catch them all. But I think that it's more of, like, a sanity check. Like, they didn't…
You know, add a new workflow that runs some binary they uploaded, or something like that.
So, just take a peek, if anything, at least that's what I do. If there's nothing obvious, I just click allow.
**Jared Freeze** 17:29 Okay, cool. I'll do that and start the review then, because it won't pass in its current form.
I had one other thing to mention, if nobody has anything specific, but I submitted a PR to the core repo to remove some old Safari sort of patch code, which was the navigation timing level 1,
fallback, because OTEL requires Safari 15.4 and up, which was released in September of 2021.
I'm not super worried about it, it did get merged.
The reason I wound up making that PR is because I'm working on a validator that looks through the disk folders and the build folders to assert that we are not using anything that's not widely available according to baseline rules.
And what I found is that the source code is straight. The disk code is not.
Because it has things that are coming from all these other vendors, right? Which makes perfect sense, but I kind of didn't really think about it right away. And one of those things was this code, because it's too old, and so it has been marked as not widely available.
There are actually 7 items, that are on the list that we've all agreed to, but I will be updating the documentation, because I made the, sort of assertion that, like, oh, widely available should actually be our goal, right? Like, we shouldn't really use, like.
strange stuff, but there's so much useful stuff that we talked about accepting that is Google-only, or whatever that,
I'll be updating the docs there. So, just a heads up that I found a lot of really interesting stuff, so I'll post the results later, but
But yeah, like, Web Vitals has tons of stuff in it that's got, like, if… if I'm Chrome, do fun stuff, else don't. But the validator doesn't know that, right? Like, it doesn't actually check for conditions, so…
Yeah, kind of technical research.
And one other thing I can mention, so I converted the entire core repo to use TS down instead of, TypeScript.
And it doesn't work because of the barrel files?
So, it's pretty cool that it builds in, like, 500 milliseconds, but it doesn't work. So, if we were able to issue barrel files, we'd be in a pretty sweet spot. Yeah, you let me know what you want to do, Daniel.
**Daniel Dyla (Dynatrace)** 20:03 I can also build something in 500 milliseconds that doesn't work.
**Martin Kuba** 20:06 It's…
**Daniel Dyla (Dynatrace)** 20:07 I don't know what a barrel file is, maybe I'm missing some context here, but is it… is it the type of thing where you're like, this is a dead end, or is it the type of thing where it's like, maybe there's a workaround?
**Jared Freeze** 20:20 Yeah, the index.ts. So it's basically where you take everything in a folder and hoist it up, so people can have, like, prettier paths, so you don't have to go to every file.
**Daniel Dyla (Dynatrace)** 20:29 Got it, okay. Yeah, so I actually do have opinions on this. That barrel file, or like, where you have the index.ts that just imports a bunch of things and re-exports them, is a massive source of, compilation slowdowns and startup latency.
It's less of a problem when you have a bundler that bundles everything into a single file.
But… It's actually crazy when you profile a JS, a Node.js startup.
With the… with the… Hotel enabled.
How much of the startup penalty is actually just requires, and how many there are, just to load
like… Anything. At all.
So, it's where startup latency is actually a problem for us, you know, Lambda comes to mind. There are a lot of situations where that matters.
And I would personally be in favor of removing barrel files purely for the performance benefit that you would get.
From not having those, like, excess requires that don't really do anything.
And moving instead to…
You know, just to reduce the number it requires, I guess.
I guess…
One question I have is, why aren't they supported? Because all it is is importing and exporting. Seems like the type of thing that should
work just fine. I don't understand why it would not work.
**Jared Freeze** 22:12 And then… Oh, go ahead.
**Daniel Dyla (Dynatrace)** 22:14 Go ahead. No, you go ahead first.
**Jared Freeze** 22:18 Yeah, so it's because it tries to optimize, and what it winds up doing is creating circular dependencies.
Because…
it will… it'll, like, hoist certain things in certain ways. Like, basically, if it sees, like, exports… like, the first export, and then the barrel export get combined.
And then it creates circular dependencies. So, it doesn't know not to do that, so it winds up including more than it would had, like, it been ESBuild, which is tree shaking it out.
So, it kind of does their optimizations in different ways, expecting different things, but barrel files are, you know, an anti-pattern at this point. It's not recommended any longer, so… and just for the reason you're saying.
**Daniel Dyla (Dynatrace)** 23:03 Yeah, so I'd be in favor of that purely for the performance benefit, and then if it enables this…
I would also be happy with that.
The second thing I was gonna say is that I think my…
personal opinion and approval on this is going to probably matter less in the future. I don't know how much longer I'm going to be a maintainer.
**Ted Young** 23:30 What, what?
**Daniel Dyla (Dynatrace)** 23:30 I'll still… I'll still be around. Don't… don't worry about that. I just…
I haven't had the time to dedicate to it, and there are other people who are spending more time than me who are not maintainers.
And it shouldn't be that way.
We'll see.
**Jared Freeze** 23:56 Is that something I should, like.
Make an issue for it and pursue.
Like, removing barrels.
**Daniel Dyla (Dynatrace)** 24:02 Removing me as a maintainer?
**Jared Freeze** 24:05 Yeah, just PR, just delete.
**Daniel Dyla (Dynatrace)** 24:08 I would be in support of it. I don't know how any of the other maintainers feel. It's not something we've talked about, so…
**Trent Mick** 24:17 Yeah, go for it.
**Ted Young** 24:19 I mean, you guys are doing a, like, SDK 2.0 thingy right now, right?
Like, oh no.
**Trent Mick** 24:26 Yeah, we're done now, we're doing studio.
3.0.
**Ted Young** 24:29 Okay. Well, I mean, we feel we have to…
**Trent Mick** 24:32 Jump that major version, at least.
I don't know, so many of the packages are still in 0. that it's not actually 3.x, but the ones that are stable would move to 3.x when we're dropping major Node versions, which Node likes to do every couple of weeks, so…
It's hard to keep up.
That's a joke, but yeah, so in June, we expect to have a 3.0 and drop node 18 and node 20.
Yeah.
**Ted Young** 25:01 Yeah.
**Joaquín Díaz** 25:02 I don't know how many…
**Ted Young** 25:04 If your priorities were still, like, clean… internal cleanup or something like that, this sounded like something that could be part of that mandate. That's all I was…
**Trent Mick** 25:11 I don't know that dropping the barrel files impacts users at all, does it? There's no…
**Ted Young** 25:18 Well, the startup costs you were just talking about.
**Trent Mick** 25:21 Oh, I mean, that's… but that's a performance one, so it's… that's a… yeah, but I don't know if it's a thing that we need to hit on a major version.
**Ted Young** 25:27 Oh, yeah.
**Trent Mick** 25:28 Unless I'm missing something.
**Ted Young** 25:29 I meant more like, you guys were…
Sounded like you guys were doing an initiative around focusing on
Like, let's stop feature work to focus on cleaning things up internally, but maybe that's over with.
**Trent Mick** 25:44 Yeah, kind of over what's… yeah. I wouldn't say that we're totally organized in what our priorities are, but, yeah.
Yeah.
**Joaquín Díaz** 26:00 Should we also remove them from the browser? I don't think we have many, or I don't even know if we have some, but…
Now we… we don't have to be… do… do a heat refract process.
If we've had some, it's just a few. We just… we should remove them.
**Trent Mick** 26:19 Am I wrong that there's no user impact? Are we forcing changes on the users by dropping… I don't know if it's, like, just the internal barrel files. If it's the single top-level one.
Then it… Is there an impact on the… on the user?
**Jared Freeze** 26:34 Well, so since the, since OTEL's not, like, true ESM, like, since it's not valid ESM, there is a chance that somebody was able to deep link to a file, like, they're actually going to index.as.
Yeah.
**Trent Mick** 26:51 No, we screw them and added exports for some other reason, but yeah.
**Jared Freeze** 26:55 Exactly. So, I mean, if we… if I… I mean, I would actually like to do that work. I've done it a few times, like, just messing around, but, adding exports and getting rid of barrel files and doing all those sorts of things, will prevent people from doing this deep linking, so… I don't know if there's even a way to find out how many people really do that.
In the book.
**Joaquín Díaz** 27:18 I didn't have to, like…
isn't the, like, the official artifacts of a package is what is coming from the top-level package, right? If you're doing the…
level in Burton, then that's up to you.
**Daniel Dyla (Dynatrace)** 27:31 Yeah, in the past, we've made changes that have definitely broken people doing that, and said specifically, this is not something we ever promised we wouldn't do.
Like, we've added some,
Some of the exports that prevented the deep linking in the past, and we just said, that's fine.
**Trent Mick** 27:57 Yep.
**Jared Freeze** 27:57 So you're not waiting for a major, then?
**Daniel Dyla (Dynatrace)** 28:00 For that.
**Trent Mick** 28:01 Probably not, no.
**Daniel Dyla (Dynatrace)** 28:03 I mean, it depends how far out the major is. If… If…
We're close to a major version release, and it's just, like, a nice cleanup thing, then…
you know, it can be viewed as breaking, putting it in the major version release might, you know, just make people less likely to yell at us, but honestly, I…
Not that worried about it.
**Trent Mick** 28:35 I guess, yeah, I guess my suggestion would be start small to show exactly what your
what… what the impact will be, because I'm worried that I'm…
saying, yeah, go for it for something that I'm misinterpreting how much of an impact we're talking about putting on users.
**Jared Freeze** 28:53 No, that's fine.
**Daniel Dyla (Dynatrace)** 28:55 The primary question is if a user follows the documented examples and imports it the way that we tell them to import it, will that user have to change anything?
**Jared Freeze** 29:09 Not that I know of. I mean, these files are called, like, internaltypes.js. Like, it's very clear that you're not supposed to be doing this.
The reason I've been thinking about this is because we actually do this.
But also then this TSDAM PR, so we'll… I mean, we'll figure it out on our side, like, as a vendor, but,
I do… yeah, I didn't even really consider the performance. It was really more about compatibility with newer, modern tools, because they're doing optimizations that just sort of break this pattern.
But yeah, I'll do a small one, and then send it out, so…
**Trent Mick** 29:45 Okay, cool.
**Daniel Dyla (Dynatrace)** 29:47 Yeah.
the performance thing, I became aware of it a long time ago, are… we used to create a, requoire-in-the-middle wrapper for every single instrumentation.
And what that does is, like, every instrumentation would re-wrap require, so every time require was called.
It was calling the wrapper version for every single instrumentation on every require in your entire application, and it was causing, like, 3 or 4 seconds of startup latency, and, like.
In some slower instances, was double-digit seconds.
And we were able to improve that.
like… Several orders of magnitude by re… by, you know,
Now we just reuse a single wrapper that Yeah.
that I became aware of.
**Trent Mick** 30:41 Middle Singleton thing.
**Daniel Dyla (Dynatrace)** 30:43 Yes.
**Trent Mick** 30:44 Yeah. Yeah.
**Daniel Dyla (Dynatrace)** 30:45 I became aware of the impact of the requires at that time, because I was profiling the,
the startup impact, and I found even our optimized version, which is way, way, way better, not just our application, but, like, in general, start up any application requires is, like, 80% of the startup cost of every application.
**Joaquín Díaz** 31:13 Yeah, I think it also makes tests slower, because they also have to load a bunch of things that are on the index files when you run them.
Spice is the same thing.
**Trent Mick** 31:26 Nope.
**Daniel Dyla (Dynatrace)** 31:35 Well, I think we're over time.
I don't have much else to say about this topic, anyway.
**Jared Freeze** 31:45 Well, I hope you come back, Daniel.
**Ted Young** 31:47 Yeah.
**Daniel Dyla (Dynatrace)** 31:48 I… oh, no, it's not… I'm not going away.
I'm not going away from this group, I'm not going away from JS, I just have less time to dedicate to it these days. Like, over the past several months, Trent can tell you I've been not working on JS, so there's no reason for me to keep the title more than anything. It's more about the title reflecting
Reality than my day-to-day actually changing.
**Ted Young** 32:13 Nice.
I think this is the last meeting of the year as well, right? We're gonna shut down for 2 weeks.
So, see you all in the new year.
But I'm really stoked. I feel like, you know, browser laid fallow for a really long time, and we've now, like, resurrected it from the dead, and it feels like there's good velocity and momentum, and it feels like a real project.
That's awesome.
**Jared Freeze** 32:48 Yeah, it's pretty exciting.
**Ted Young** 32:50 Yeah.
**Trent Mick** 32:52 Boom.
**Jared Freeze** 32:54 Have a good break, everybody.
**Martin Kuba** 32:56 I'd have to tell me.
**Ted Young** 32:57 I like leaky maca.
**David Luna Bistuer** 33:00 heavier.
**Ted Young** 33:01 Let's see ya.
