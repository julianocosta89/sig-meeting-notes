SIG: Browser SIG
Date: 2025-11-13
Duration: 37 minutes
Zoom Recording URL: https://zoom.us/rec/share/U94HfhEvEvtj4hIHe6GeOLK1BaagBpwH6-T5P07yjHw6CK3qLjOMJOYZ8uz2Fota.wye_tv12NQkh7bsH
============================================================

## Zoom Recording Transcript

**Jared Freeze (embrace)** 00:59 Cheers.
**Martin Kuba** 01:00 There.
**Jared Freeze (embrace)** 01:02 cold.
**Martin Kuba** 01:05 It's more like, early… too early in the morning, I haven't brushed my hair yet.
**Jared Freeze (embrace)** 01:10 Yeah, for sure.
**Martin Kuba** 01:13 I get that.
**Wolfgang Therrien** 01:22 Hey, folks!
**Jared Freeze (embrace)** 01:25 Hey.
**Martin Kuba** 01:29 They're…
**Jared Freeze (embrace)** 01:36 So, they said… so is CubeCon happening right now? Is it gonna be late today?
**Martin Kuba** 01:43 Yeah, I think so. I'm not expecting Dan or Mark to join.
Boom.
But… Yeah, I don't know about…
Not everyone goes to KubeCon, so I'm not sure.
I think it might be actually useful to have,
Can I just, like, if you have just more of the core group this time?
Just gonna sink on things that we have in progress, and… And see where we can…
Gonna put our focus on to keep things moving forward.
Sometimes, sometimes these discussions, like, we have only half hour, sometimes these discussions… Kinda go into random topics.
**Wolfgang Therrien** 02:58 Yeah, they get very strategic and less tactical, for sure, sometimes.
**Martin Kuba** 03:04 Yeah.
**Jared Freeze (embrace)** 03:07 Agreed.
Cool, it's 1033. I say we go for it, Martin.
**Wolfgang Therrien** 03:13 Yeah.
**Martin Kuba** 03:15 Yeah, I mean, so the first topic I put there, and I just think it's…
For me, this is a big deal, actually, for Wolfgang, that it's… that it's this… this… this instrumentation has been merged, because it's the first one that actually emits events.
And we've been talking about, you know, emitting events for, like, years. Like, literally.
**Wolfgang Therrien** 03:39 We are so excited to have contributed it. You know, big shout out to Purvy, who's not here today, but she was also instrumental in getting this, getting this out, and I'm excited to do the next one, Core Web Vitals, which I think, you know, we have an implementation that uses traces, and I think, events is going to be…
you know, a better fit for it, so we're… we're super excited. Thank you.
**Martin Kuba** 04:01 Yeah.
And others are coming very shortly, but this is the first one, so I wanted to just acknowledge and celebrate, so…
**Jared Freeze (embrace)** 04:09 Yeah, very cool.
Cool. Okay, well, I was just having a discussion, to jump in.
I was looking at just, like, practicality, so there's no semantic convention for, like, stripping stuff off of a URL, and so I thought it might be nice to have, like, again, a practical solution, which is, like, no hash, no user pass, which I haven't seen in, honestly, 20 years, but I know it exists.
No, you know, literally just the path, right? Like, strip off all the things that may be tracking, or, you know, you know, or…
you know, links within the page, obviously, with the hash change. Now, it leaves out certain…
possibilities. The one I called out on the previous PR was, like, I know that some of the CDNs, you can change image size with a query string.
PBD on, like, if people want to keep that or not, I thought it might be a nice idea to have a, canonical, and then have a query string as an optional attribute, url.query, and then if you needed that information later, maybe you could pick it up at that point, but at least that way you'd say, like.
hey, here's all the hero images. Like, it is the same image, it's just like, oh, it's mobile, or it's this, or it's that, so…
it might throw off things like file size, but it would be really good as far as, like, what is the asset? So I thought that was a nice division of, sort of, how things might go.
I don't know much about the semantic convention side of things, so this was really just, like, a… just an idea I had that I was gonna put up for discussion, so that way, when we… I got ready to sort of propose it to whoever it needs to go to, I think it's just a larger group than…
If you guys agree, it's a good idea. You know, we can take that to Slack or not, but I wanted just, again, to use our document as, like, a place to just keep track of, like, what we're doing.
Like Martin was saying, just for…
You know, what things are in flight, or whatever, so…
So yeah, we can do that now or later.
It's up to y'all.
**Martin Kuba** 06:10 So, so there are existing semantic conventions.
That, like, split all these things into, like, individual parts. Let's see…
**Jared Freeze (embrace)** 06:21 So I looked on HTTP, there's nothing specific to the… to…
I… to… to exactly this, is from what I… from what I saw. I may have been looking in the wrong spot.
**Martin Kuba** 06:36 Yeah, hold on,
So… Like, this… I was thinking this one.
this URL…
**Jared Freeze (embrace)** 06:59 Yeah, so…
Oh, no, I was just gonna say, yeah, so there's nothing here that's… that's origin and path.
I thought that might be good, because that's, like, for the resource timing,
I don't know, I just thought it might be nice to not have to, like, concatenate later when you're gonna do it, like, 100% of the time.
**Martin Kuba** 07:21 Hmm.
**Jared Freeze (embrace)** 07:21 You know, that was kind of my idea.
**Martin Kuba** 07:26 I think it makes sense, yeah. I mean, you can certainly propose it.
And, yeah.
**Jared Freeze (embrace)** 07:34 Cool, and that's just, like, a different SIG, or should I just do a PR? Like, just straight up PR to the repo, or something?
**Benoît Zugmeyer** 07:41 So, we'll want both the full URL and the canonical one without… The, the pa- the… Documents, or…
Do we just want the canonical one?
I'm just worried that we would send the same information twice.
Sending the full URL.
for… to me, it's always better, because the rest of the parts of the… all the parts of the URLs can be passed.
At ingestion time, by the backend.
And indexed, separately if we want to do analysis on those.
So I don't think we really need to do it on the client side. That's my point.
**Jared Freeze (embrace)** 08:40 Yeah, and I think that's what, sort of, everyone does today. So yeah, if there's not a use case for it, that's… that's fine too. It just seemed like,
you know, reducing cardinality in this spot might be good, but yeah, this is exactly what I asked.
**Wolfgang Therrien** 08:54 I think there… I think writing up the use cases is a good exercise, right? We have…
talked about writing up the use cases of why we might want supporting semantic conventions. I can see a use case for this, because I think a lot of front-end teams might not own back-end infrastructure to do that parsing at InGIS. They might just have access to the client, and they might be sending it to a third party where they might not have the resources to set it up, so giving them a semantic convention that they can lean into, or maybe the instrumentation can be configured if sending
the volume of attributes is a concern for you, right? So it might still be worthwhile to propose it, and then we can figure out what
levers we need to tune at instrumentation, right? Because maybe it's not required, maybe it's recommended, maybe it's optional, right? But I think that's true of a lot of front-end
teams where they're like, I want this thing, and I don't have the ability to parse out the full URL, so therefore my dashboards aren't, terribly useful, because they don't… maybe don't own the telemetry pipeline, or they don't have any, resources to…
To get the… the information at the granularity that they need.
**Jared Freeze (embrace)** 10:03 Yeah, that's a good point. I'll make sure to, to put something together for that.
**Martin Kuba** 10:09 You know, so I would say, like, it, like, that doesn't necessarily mean that it needs to be collected from the instrumentation side.
Like, you could have… you could have, like, a…
A processor in… in the collector.
that, like.
that takes… takes the full URL, and then splits it into parts, and then sends it off to the backend.
Like, so you would still need the… Symante conventions for those.
for that.
Thing that you want to parse out.
So, it might still make sense, yeah.
**Wolfgang Therrien** 10:41 That also can give users that…
that ability to, like, maybe start sending it from the client, and then once they have, like, sort of justified the expense or the resources required, they could spin up that collector, or maybe they're taking it out of a development environment into a production environment, right? And it gives them the ability to maintain that semantic convention, regardless of how it gets populated.
**Martin Kuba** 11:02 Yeah, yeah.
**Jared Freeze (embrace)** 11:04 Cool.
Just gonna copy that link to the doc.
I will make that my homework.
**Martin Kuba** 11:28 Does anyone else anything else? Anything else they want to talk about?
**Joaquín Díaz** 11:34 No, just a reminder… I'll… I want to get that PR merch.
The one of the instrumentation, so if you want to take another look today.
The ones who didn't, otherwise all merging this, like, end of day, so we can keep moving with the…
build steps, testing steps in CI.
**Benoît Zugmeyer** 11:56 I just left a very… Small comment, but…
**Joaquín Díaz** 12:00 Yeah.
Yeah, no, thanks, I really appreciate it. Thanks.
**Jared Freeze (embrace)** 12:08 Yeah, I got some good feedback on the turbo, Pr as well.
So I'll address that. I think it came yesterday, maybe the day before, I just haven't had a chance. And I'll get that updated, and then if Joaquin gets, his stuff merged, I think some of the turbo stuff is actually in that PR because he branched off, but, it'll help unblock, because it's not actually, you know, there's nothing running at this point, none of the…
you know, sort of tests or things like that. So, then I'll have something to act on, and then hopefully it'll unblock a couple more of those things. So, that was kind of my idea. I don't know if that's, like, the proper way to do it, to have instrumentation before we're actually testing it, but.
**Joaquín Díaz** 12:48 No, so…
**Jared Freeze (embrace)** 12:49 You gotta start somewhere, right? So…
**Joaquín Díaz** 12:51 Yeah, I also have a test harness branch.
repo that I did a while ago that was empty, I can also have that.
And, I added, by test browser.
to the test that I'm running on the instrumentation, and it works very well.
So yeah, we can keep using that as well.
**Jared Freeze (embrace)** 13:16 One other thing to add. I actually added a Webpack 4 test to Contrib.
Or it's… it's on its way. Mark had some feedback as well, but,
I think the idea at a certain point would be, like, move that over, and that might be a good way to test our test harness running in the contrib repo, you know, where we're pulling in stuff off of
main or PRs or whatever, like, if they're able to import that action, because that was an idea I had, I'm not sure if it's viable, but, I thought it might be nice, so that way we control that code, but it's actually running, the test suites in the other repos, so that way they don't have to manage that stuff, or, like, try to keep things in sync.
So, it'd be a nice little bit of research to try to figure out over there, so…
**Benoît Zugmeyer** 14:10 Yeah, I… I'm planning to write a, to propose, A new resource to… convey the…
To link together all the telemetry that is being sent from a single document, as
So, I'm thinking about, document.id, something like this, similar to a session.id.
But for the running documents?
So when we have multiple tabs or iframes, We can still…
Kind of group things that happens on the same document.
Do you think that's a good idea?
R.
Any feed… early feedback?
All that.
**Jared Freeze (embrace)** 15:04 Yeah, so at Embrace, we already do this, across tabs. It doesn't have crosstab
communication exactly, so it's not using, like, broadcast channel or anything like that to keep in sync. It's actually got… it's a little bit of a race condition for opening new tabs and, like, stringing them together. So I'm not sure if that's exactly what you mean, or if you're talking about just, like, in the same, like, tab or window.
**Benoît Zugmeyer** 15:30 Yeah, just… similar that what, what the notion of documents, Martin brought in the navigation.
event.
There is this same document, attribute.
And I like that idea that we think about like, a document that…
It can have multiple URLs, navigation changes, right?
But in the end, it's the same document that has been loaded
First, and then, it's running.
And so, yeah, it's just, like, when the page is loaded, we…
We throw a dice, like, we get a random number, and we keep using it for the rest of the…
Document lifetime.
Would you.
**Jared Freeze (embrace)** 16:30 Would you expect that ID to survive across a hard navigation load on the same URL? No. Okay.
**Benoît Zugmeyer** 16:37 No.
That would be a new document.
**Jared Freeze (embrace)** 16:41 Cool.
**Martin Kuba** 16:42 So I think that makes perfect sense. I think,
You know, it gives additional context.
I would… So maybe, like, maybe, Benoit, if you don't mind opening an issue, and…
like, I think it might be helpful, like, to describe the use case, or use cases for using this.
You know, like, what… you know, like, what you're thinking about…
Yeah, how that would be useful.
But I think that it does make sense, yeah.
**Benoît Zugmeyer** 17:12 Okay.
I will do.
**Abinet Debele** 17:17 Hi, I also, like, also like, some more reviews for the browser navigation instrumentation.
Amit, some additional changes based on the comments and,
Also, the build was failing, now it's working fine, so…
Just take one more look and,
we can also merge that one, and if you need, like, I can also make a quick demo, maybe next week.
If you think that's, that's good.
**Jared Freeze (embrace)** 17:56 Sounds good. Do you mind adding the PR link to the Google Doc?
**Abinet Debele** 18:02 Oh, okay, I understand.
**Jared Freeze (embrace)** 18:04 Yeah, that'd be helpful.
**Martin Kuba** 18:08 Yeah, I think, Benedict, this is a great idea to do a demo.
I, like, I do have… I do have some questions and comments, and I think I reached out to you directly, but I think getting feedback from everyone in the context of actually looking at it would be… would be helpful, I think.
**Abinet Debele** 18:29 Yeah, that sounds good.
**Martin Kuba** 18:32 You know, I think this, this whole, we have, we had a lot of discussions about this, about the, you know.
We kind of pivoted from… The page is…
Page view, instrumentation to navigation instrumentation.
**Abinet Debele** 18:46 Yay.
**Martin Kuba** 18:47 There's also… some… Still maybe some… gray area about…
The use cases for the navigation instrumentation, because…
Because there's… it captures, like, a lot of different… Types of navigations that
might be used differently, like car navigation, spa.
navigation, and also just URL changes.
That don't represent necessarily navigate, like, logical navigation, so…
I think, you know, having that discussion would be very helpful.
**Abinet Debele** 19:24 Okay.
Yeah, so I… yeah, for next week, I'll… I'll try to, do that again.
**Martin Kuba** 19:32 Great, okay.
Would it be helpful, like, if you were to take a quick look on… at the board and see…
What else is in progress? What else, if anyone needs help with anything else?
If anything's missing that people are working on?
**Joaquín Díaz** 19:57 Yeah, sure.
**Wolfgang Therrien** 19:58 Yeah, let's do it.
**Martin Kuba** 20:02 Share my screen.
So this, the… this one, the… that's done, right? Or at least, like, the initial… To define broad.
**Joaquín Díaz** 20:39 Yeah. Pinnacle list.
**Martin Kuba** 20:42 I think…
**Joaquín Díaz** 20:43 We also wanted to have some… something written down around…
Baby philosophy of what we capture.
more than a list, but I don't know if that's in another ticket, or if we want to keep the same ticket.
**Martin Kuba** 21:00 Yeah, I would probably say, let's open a new ticket, if there's something else that needs to be done.
**Joaquín Díaz** 21:06 That's weird. Yeah.
**Martin Kuba** 21:08 Or maybe, like, yeah, I think that's probably better.
Let's see…
So, okay, if I move this to done…
**Joaquín Díaz** 21:22 Yeah.
**Martin Kuba** 21:33 So this… this… I'm gonna leave this page view event open. It's… it's essentially the same as the navigation… navigation one.
This navigation instrumentation.
So that's in progress… still.
This one, actually… That's assigned to me, but… So this…
I was going to, like, I think the only instrumentation that's not
actually being worked on yet is the navigation timing one.
That we have planned on.
Is… wasn't everyone planning on working on that? If not, then I was gonna take it.
**Joaquín Díaz** 22:21 Oh, I think you got taken.
**Martin Kuba** 22:25 Okay.
I think this is the semantical mention, and then there is the instrumentation here.
Okay,
I guess, is there anything missing, like, in what's in progress that people are working on? Should we add…
Should we try?
**Joaquín Díaz** 22:47 Awesome.
**Martin Kuba** 22:48 Sometimes.
**Joaquín Díaz** 22:49 I don't know if we should track, like, all the set dot…
the chair is doing with Turbo.
and then we will need another ticket for…
like, setting up a CI to run the tests on PR, on stuff like that.
maybe another one for the test harness, and then eventually one for… Publishing the first package.
part of the repo. So those… I don't know if there are tickets for that.
**Martin Kuba** 23:26 Okay.
Would you mind creating those tickets?
**Joaquín Díaz** 23:29 No.
**Jared Freeze (embrace)** 23:30 Yeah.
Yeah, we'll make those.
Another thing, I was doing a little research on, like, baseline widely available in ES2022, because we had talked about that. I know OTEL chose ES2022. On the browser side, obviously, we have browser support, which is not
Node doesn't care about that at all. So, there's an ESLint plugin, that somebody just made, or there's a Google Hackathon thing going on a couple months ago, and so it's an ESLint plugin that checks baseline. I ran it in Contrib, so I have a, draft PR I can,
Blink 2.
And, long task is technically experimental, and there's long task instrumentation, so if you were to run that in an
you know, error instead of warn, like, the contrib repo, the CI, would fail.
So that'll lead to a longer discussion, but, I think it's kind of tied to, like.
kind of part of the bundler work a little bit, like, what recommendations for export or whatever, like…
you know, what's available, right? Because Acorn is…
you know, the thing that sort of ingests code, so Webpack 4 can't read anything over 2018.
without plugins. So it's like, we can say Webpack 4, but, like, it also needs plugins. So I think just, the work around describing what code we're going to export, along with what bundlers we support, I'll make tickets for that as well, because I do think that
is a really separate concern. It's like, what are we… what are our… what are our targets? What are we gonna export? And what do we say we support, as far as…
the… you know, again, what you're actually going to use in your application to build, so…
Yeah, I think that's probably 2 more tickets.
Long task is interesting. I'd actually like to go look and see, like, what… what kind of life that had, because it's only available in Chrome.
So, not that I don't think it's useful, but, like, how… you know.
How much appetite is there for, like, things that are truly experimental?
Right? Because, you know, we've been talking about this at, you know, Joaquin and I on our side, with,
Render blocking status is incredibly useful.
it is only available in Chrome, so, you know, maybe we should have a discussion, too, about
Do we really want to…
support things that are only available in Chrome. We want to be more conservative, you know?
Practically speaking, of course, we all know it's 80% of the world, basically.
**Joaquín Díaz** 26:06 I think, yeah.
**Jared Freeze (embrace)** 26:07 because of Android. But, you know, is there a philosophical reason, potentially, in hotel that I don't know about, that's like, you know, we're, you know, we keep things a little more, a little more,
**Joaquín Díaz** 26:20 you know, pure… That's how we practice.
Yeah, we had this discussion already, and I think we agreed on
Including things that wouldn't block the runtime for users.
So,
Like, going back to example of the render blocking, like, it's fine if it is missing for 20% of the browsers.
as long as the code that is trying to get it wouldn't break on those browsers, I think it's fine, like,
I think we should be practical in that way, and…
like, I know they're seeing that most people is on Chrome, so… We shouldn't,
miss that information for 80% of the users, as long as it's not breaking the runtime of the SDK, or the…
**Jared Freeze (embrace)** 27:06 Yeah, yeah, perfect. Okay, so then, really, the ticket is get it into Docs in the browser repo.
**Joaquín Díaz** 27:13 Yeah.
**Jared Freeze (embrace)** 27:14 Because it's kind of… yeah, you like, yeah, Benoit just linked to it, but, I forgot, and we didn't write it down. So, cool. Sounds good.
**Joaquín Díaz** 27:23 Yeah, I can create a ticket, to write that document. Like, document it somewhere, so…
Anyone coming into the repo knows our approach on that.
How we capture things.
**Martin Kuba** 27:43 And it's like, we have some instrumentations that are in Contrib.
We have some instrumentations that are in the JS core.
We're now introducing some instrumentations in the browser repo.
I think that the way the JS SDK is set up is that, like, some core… I mean, the core parts, obviously, are in the JS core, and then, like, users can…
Can, contribute, like, their own…
kind of non-core instrumentations in Contrib? I mean, do we want to have, like, the same kind of…
Concept here, or… We're talking about, like.
Having anything that's in the browser repo is gonna be… The things that we, like.
That we, like, consider being, like, key for… Only.
Or, like, should we have also, like, experimental, or… contrib level.
**Jared Freeze (embrace)** 28:44 It might be nice to have contrib in the browser repo. So, like, not a separate… not, like, another browser contribib, but maybe just the folder that's, like, core package, and then contrib package. So that way, you have the benefit of…
You know, having them all in the same place, running the same tests.
**Martin Kuba** 29:00 Yeah.
So, like, I'm just sharing this, there's an existing long-task instrumentation that's based on spans, right? I don't know if anybody's really using it, to be honest, but…
It's been there forever.
**Joaquín Díaz** 29:17 Yeah. I, I agree that…
If it can't be done, it doesn't need to be several repos, etc, because we'll have to set up everything twice.
And we can keep maintaining only one pipeline, which is the main repo.
**Martin Kuba** 29:32 Good.
**Wolfgang Therrien** 29:34 I think it's really useful to have a place for maybe, like, those more mature experiments where, like, maybe it's an experimental API, but it's really valuable, and we need some place to prove it out, and a place to share that code.
that feels like a contribib or an experiments package in, the browser repo to me, so I like that idea, Jared.
I don't see a good reason not to do that.
**Jared Freeze (embrace)** 30:02 Yeah, I'll keep it a little cleaner, so it's…
Not in the, again, sort of… You know, more core stuff.
**Wolfgang Therrien** 30:09 And I think, you know, if we can just make it super clear, like, what is in Contrib and is maybe less supported, we're gonna get less eyes on it, right? It's gonna be, you know, something that…
you're gonna have to come and lobby, you know, for eyes for it, like, right? Because it's maybe not going to be something that we're going to be as paying as close attention to. Sometimes that can get, especially across repos and everything, that can be a little bit more confusing. So if we have strong documentation that says, hey, this is why this is in… this is why this is in Contrib and not core.
That I think, can be really helpful, too.
expectations.
**Martin Kuba** 30:48 Yeah, yeah, exactly, and I think the distinction that the JS maintainers make is that
Anything that's in Contrib is not actually maintained by them, by the maintainers. It's like they… those packages need to have owners.
like, assigned… So I think it will come down to, like, what do we actually want to support?
Yeah.
**Wolfgang Therrien** 31:14 I think that's a reasonable model, and that's probably one that a lot of folks who contribute are…
are used to, so we can adopt that and see how far we get. If we need to diverge, we can address it later.
**Martin Kuba** 31:27 Okay.
**Jared Freeze (embrace)** 31:30 Yeah, it sort of reminded me, too, we need tickets for migrations, for the older stuff, because we do have to sort that out, so we should go one by one on… down the list, on our homepage, and…
Yeah. Have, you know, collaborate on that.
**Joaquín Díaz** 31:45 I think we need to do one.
Once we have the setup to publish, we have… we need to do one end-to-end to see how it goes, and document that process, and then…
Keep doing the rest.
**Wolfgang Therrien** 32:03 That sounds like maybe there's, like, two tick… like, two tickets, like, one to document the process for migration, because we're going to have to do, you know, maybe a dozen of these, or more.
And then the second one is to, like, break out the rest of the tickets for those follow-on… maybe the… I don't know if they're…
sub-issues or other, like, top-level issues or whatever, but, like, to draw the rest of that owl…
**Joaquín Díaz** 32:27 If.
**Jared Freeze (embrace)** 32:28 Inversioning, we still have to talk about versioning.
**Joaquín Díaz** 32:32 I think… Well, we have to talk about it. I think… From the last meeting, we…
Acknowledge that, at least the instrumentation packages, they don't need to follow the same versioning as the one they follow now.
So we can decide whether we start doing that.
1.0, or… 0. something until we feel like they are, like, not experimental.
A lot of those packages have been experimental for years, so I think it's time to
For most of them, just moved on to… Take care.
1.0 release, and start working from there.
At least on the instrumentation side.
**Wolfgang Therrien** 33:19 That sounds like a good thing to call out as sort of, like, open questions in, like, the issue for moving an individual, like, instrumentation over. It's like, should this be moved… if it's experimental, should it be moved to 1.0? Like, should it be in Contrib? Like, where, like, or is it…
stable enough and widely used enough to go into core, like, do we want to take on that ownership, right? I think that's a good list of questions to… to address sort of that one at a time.
I must… We know the answers to all of those questions at once.
**Joaquín Díaz** 33:52 Yeah, I think…
For the first one, we should find the most easy, small, and the one that for sure we know we want to make it, $1, $1.0… yeah, $1.
a bullish our one, then we see the others.
**Wolfgang Therrien** 34:10 Does anyone have a good suggestion for that off the top of their head?
**Joaquín Díaz** 34:17 I'm going through the brief right now.
**Martin Kuba** 34:22 So, so I know that'll probably… I don't…
Might need some… might need some guidance from…
like the JS maintainers, or maybe from someone You know, from,
Who knows more about this, but…
I think there's also maybe some prerequisites, like the instrumentation cannot go stable until the semantic conventions that it emits are stable.
And also, like, we need to, like.
Commit, like, the support, maybe, like…
like, supporting it might be more involved, I'm not sure.
Like, one thing that we haven't… I feel like we haven't quite settled on in this… in this group yet is… is, are we actual maintainers? Like, like, do we have, like…
Dedicate maintainers that are committed to this?
Because, like, we should probably, like, document that, and then…
you know, just to make sure that, like, we know that those people have those responsibilities. I mean, it's not just, like.
So we can rely on, those packages to continue to be maintained.
Do we want to put that as an agenda item for next time? Because I think we're a few minutes past. Yes, yes, that would be… I think that's a good idea, yeah.
**Jared Freeze (embrace)** 35:42 Hopefully Ted will be back as well.
**Joaquín Díaz** 35:46 about the conventions, I have the same thoughts, like, if the experiment has been out for a few years.
And these experiments, all the same applies to semantic omissions, like.
They should just move… be moved to…
Stay stable, if nobody changes them for, like, 3 years.
I don't think we have a ton of packages, on the color.
repo that I feel on… on Share.
So… Maybe we got a big one for that.
**Martin Kuba** 36:28 So, I agree. Like, I'm not sure what those… what's holding those things back. So we're over time now.
So let's… let's maybe, like, move… like, move these topics to the next meeting, or…
**Joaquín Díaz** 36:42 Yeah.
**Martin Kuba** 36:43 So, like, I think we have a few action items, create new tickets, and then…
This… yeah, this… this conversation to the next meeting, so…
**Jared Freeze (embrace)** 36:54 Cool. Thanks, everybody.
**Wolfgang Therrien** 36:55 Thank you.
**Martin Kuba** 36:55 Good.
**Wolfgang Therrien** 36:56 Have a good one.
**Jared Freeze (embrace)** 36:57 Dear.
