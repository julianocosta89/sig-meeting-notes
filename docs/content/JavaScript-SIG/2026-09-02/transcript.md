SIG: JavaScript SIG
Date: 2026-09-02
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Marc Pichler (Dynatrace) 00:01:05 Hello?
David Luna Bistuer 00:01:09 Nope.
Marc Pichler (Dynatrace) 00:01:54 Welcome, everyone.
Let's say, let's get started.
The first topic here is from, Pranav.
The GenAI users library split.
Oh, Hey.
Pranav Sharma (Google LLC) 00:02:18 Yeah, I, I just wanted to ask, like, I recently had that GenAI utils library, which was too big, so I tried to split it in multiple PRs, so I just wanted to know if this size is okay for the first one.
And, also, was asking, like, if we could enable stacked PRs in this repo?
like, that could make this process a lot easier. I don't know what other people's thoughts are here.
about stacked PRs, how do they feel?
Marc Pichler (Dynatrace) 00:02:52 I haven't used them yet. I think the size… like, about two and a half K9s sounds reasonable. But stacked PRs, I'm not sure if we even… Can enable this.
Pranav Sharma (Google LLC) 00:03:11 There was some discussion in the Slack channel this, I think today, this morning.
like… Where it seemed like, you know, it was just disabled in… in contrib.
And, maybe the maintainers can… it's really a question for the maintainers, if they'd want it.
Because, without that, I don't know, like, like, I tried creating a subsequent PR out of this, but then, you know, because it was opening against the main one, that was, again, coming up with a huge diff.
So…
Marc Pichler (Dynatrace) 00:03:50 Understood.
Pranav Sharma (Google LLC) 00:03:50 unless this gets approved and merged, the subsequent PRs will not get any smaller, and that's what I was concerned about.
Marc Pichler (Dynatrace) 00:04:03 So… It does look like that, currently… Stick.
PRs don't work on PRs that are open from Fox.
Pranav Sharma (Google LLC) 00:04:17 Yes.
Marc Pichler (Dynatrace) 00:04:18 And we generally don't allow pushing to… the actual repo. Like, not even for maintainers, we do allow this, because everything has to go through the ECCLA check, and I think that's an organization-wide issue.
Pranav Sharma (Google LLC) 00:04:43 I think they do allow it, and I think… Python, but I'll have to double-check that. I thought that there was this convention which was allowed in Python, where, you know, you could push branches as long as they are prefixed with your GitHub username slash But, yeah, I'll… I'll double check that.
Marc Pichler (Dynatrace) 00:05:06 Yeah, I'll also look into that. It seems that Dan is also on it.
So let's see where that goes.
Yeah, I'm not sure I'm comfortable with… Allowing pushes to that, because if we do, then we might also have to make some changes to, like, what's available to workflow runs and stuff like that. Has some security implications.
So, we'd have to look into that as well.
Unfortunately.
Trent Mick 00:05:48 I haven't used…
Marc Pichler (Dynatrace) 00:05:49 Yeah.
Trent Mick 00:05:50 No, I was gonna echo some similar things. I haven't used them myself at all, but if they are what I dream they are, then I would like to have the functionality, because if something takes a while to review, even if it's not… if it is logically separate PRs, not just… it's a huge PR and we want to separate them, building on top of them can be helpful while the review process is going on.
Because I've been doing that for some of the declarative config work, and it ends up being, like, don't bother looking at the second PR until the first one's done, because it includes all the divs. And then… stacked PRs, I assume, aren't going to solve this… magically solve the problem of needling… needing to deal with, With merge conflicts and stuff, but, anyway, it'd be nice to… When I look at OpenTelemetry Python, I don't see any branches on the main repo.
that are from users. On OpenTelemetry Python Gen AI, I do, so maybe this is OpenTelemetry Python Gen AI. They've allowed that. Yeah, yeah. Yeah.
Similar to Mark, I don't know what the… Repo permissions requirements thing we'd have to worry about if… if anyone can push branches, I don't know if that has security implications or not. I think that's what you're saying, right, Marc?
Marc Pichler (Dynatrace) 00:07:09 Yeah, that's exactly right. The… Security… so we don't have a lot of, tokens that are, like, still in use, especially not the publishing ones anymore, but I think there might still be one or two things that we might have to rethink before enabling that.
Pranav Sharma (Google LLC) 00:07:38 Okay, all right, appreciate it. I just wanted to bring this topic up to the maintainers, and I posted the relevant conversation from Slack in the chat here, if you guys want to take a look at that, but… Yeah, that's it for my topic.
Marc Pichler (Dynatrace) 00:07:58 I'll have a look. I think general sentiment is that we are interested in having stacked PRs, because the feature looks very helpful.
Pranav Sharma (Google LLC) 00:08:09 Yeah, it would help the review process, at least for these big PRs, yeah.
Yeah, thank you.
Marc Pichler (Dynatrace) 00:08:17 Thanks.
Trent Mick 00:08:19 Before we go to the next one, because I think that's the big one, Matt, did you typically need to take off halfway through, right?
Matthew Wear 00:08:28 No, I'm… I'm here for the full meeting, so…
Trent Mick 00:08:31 Okay, because we can pull yours up, which is… Let's just discuss yours now.
Though, it's gonna be the… Same annoying thing for me. I started looking, I haven't finished looking at your thing yet. I'm guessing your changes are gonna look good, and we'll probably… Probably move forward with that, but I haven't fully gotten through. The… so, the… the secondary thing, the… the change to the read config properties that you had to be… type-based.
I can't decide on that. I have to look at the code today, but I have informed opinion. Like, certainly when it's type-based, it's nicer, because presumably completion and those things will be nicer.
in… in the IDE, rather than just the raw strings tuple thing that I had.
But I don't know if the… If the solution's… more painful than the… than the cure, if you know what I mean.
Or then the disease.
Anyway, because, I mean, like, it's… it's more involved, you're doing callbacks and stuff instead of just some static data, and it gets assigned, but… Yeah, I don't know. What did you think of the final… Reference one for the other.
Matthew Wear 00:09:43 I think both of them work. I do kind of… I slightly prefer the, typed readers, just because they're harder to mess up. Like the… the two things that are easy to mess up with the… The tuple approach is… like… Using a bad type, or, Mistyping, like, the target field, whereas, like, those two things are kind of impossible with the, It typed readers.
And…
Trent Mick 00:10:17 So that… that is why I had it fail, but if mine fails at runtime instead of build time, which is what yours would. So yeah, yeah, granted.
Matthew Wear 00:10:25 Yeah, and this incarnation of the type reader is… It's a… it's way more simple than the previous one, because it kind of… I don't know, you have, like, the… the dotted Git, and that… it kind of fuses that, whereas before, it kind of, It became, like, nested readers, and that was kind of… overly complicated, so… so I feel like this is kind of like a…
Trent Mick 00:10:51 Okay, I haven't looked at the implementation.
Matthew Wear 00:10:53 So, it's not…
Trent Mick 00:10:54 Okay, it doesn't need to do that for the nested thing there.
Matthew Wear 00:10:59 No, it kind of uses the dotted keys to, to look up nested things.
Trent Mick 00:11:04 Yeah. Okay.
What was the other thing?
The… I hadn't looked at what the implementation… Was either, but the… deep merging of things, so HTTP is… I guess the instrumentation HTTP is an interesting example in that it does have these nested config items.
I'm curious where we land on, which is kind of unfortunate. I think if I was designing a thing for config, boy, config that's flat is way easier to reason about where you should merge or not from different config sources. So, like, if… if someone does a static config of the HTTP instrumentation and wants to collect these client response headers.
And then you have a declarative config file, or central config.
or, like, dynamic config that wants to change the HTTP server, request headers.
That's, Hard to know. I guess you've done it, so it's just… it's a deep merge, and it's only the leaf nodes that will get overwritten? Is that right?
Matthew Wear 00:12:12 Yeah, previously, those were getting dropped if you were just kind of… Or if you were updating a leaf, then that whole branch was kind of getting clobbered. So, with the deep merge, you can… You can update only the leaf, and everything else stays as… as it was.
Trent Mick 00:12:31 Yep.
Okay, yeah, I guess we find out with time, we're looking at other instrumentations, what the… whether that ends up being a surprising expectation. But anyway, whatever.
So that's good. Anyway, the… snapshot is I need to finish reviewing, but it's looking good, so thanks for keeping on this.
Matthew Wear 00:12:52 Cool, yeah, thanks, and yeah, if anybody else has opinions on the type readers or not, please weigh in, like, I'm… I'm fine either way, but, But yeah, like, I pretty much took your approach and just kind of finished it off for this PR, and then I have this other branch for comparison, and if we like what's there, I can move over the type readers. If not, we can just go forward with what's here.
Trent Mick 00:13:19 Great.
Marc Pichler (Dynatrace) 00:13:26 Excellent.
Are there any, questions and comments about… this particular PR.
If not, then we can move on to the next topic, which is, Trent, about SDK 3, though.
Trent Mick 00:13:49 I thought it would be worth us spending some time reviewing what the plan is for September, so it isn't necessarily just going through every one of these, but just… If people have questions, or… Yeah, exactly how… what the mechanics are gonna be this month.
Marc Pichler (Dynatrace) 00:14:04 Yeah, one thing to note, maybe just to get everybody on the same page, you've probably seen the… SDK 3.0 announcement issue that we had pinned for some time now. It essentially contains Some of the work items that, are gonna be… high priority there, and the milestone essentially contains everything here. Plan is to start working on that.
Right now, and then finish it up by end of September, so that we can release SDK 3.2, so if there's any ideas that you have, or anything that Is a braking change that needs to go in, please feel free to let us know.
So that we can add it to the milestone.
But now we can also go over, the things that we have in there.
Yeah, so, I have seen that some things are missing still. I have this old, braking cleanup of features that don't exist in the other SDKs, where we had somewhat decided on to drop the SDK trace node package and SDK trace base package in favor of SDK Trace.
I can create issues for each of these packages, if that's okay for everyone.
Trent Mick 00:15:36 Yeah, I think that's okay. I'm trying to remember what the… because we have ST trays. I don't remember what the… killers are. David, do you know if we'll be able to get rid of the SDK Trace Web as well, or not yet?
David Luna Bistuer 00:15:49 But a little bit…
Trent Mick 00:15:52 Do you know if we'll be able to drop SDK Trace Web?
David Luna Bistuer 00:15:55 What's like, really?
Trent Mick 00:15:56 God oak.
Okay.
But, like, that's… It's gotta be this month, or it's not, or we keep… keep it.
David Luna Bistuer 00:16:03 I think so. Let me… let me check and give you an answer next week, but… but I think I'm… I'm positive.
Trent Mick 00:16:11 Okay, this is mostly about whether all instrumentations have moved over… or whether… sorry, I guess it's whether we get to a state where browser-related instrumentations in… The core and contrary pose.
no longer need to be maintained. I'm not even clear on whether we drop those yet, because everyone should be pointed over to the browser.
Instrumentations repo, or if they're different enough that we feel we should be keeping the browser-related instrumentations going.
Sorry, was that clear?
So, okay, let me start, let me say it this way. Do we need to keep our instrumentation fetch?
Going.
Or can we drop it?
David Luna Bistuer 00:16:59 We are on the way the… we're on the path of the Pranquility, so, I think it was a couple of weeks ago.
Now, a month ago, we got the fetch.
Then, I think it was a couple of weeks ago, we got XHR instrumentation, so now we have instrumentations on the browser repository.
But still, the former fetch and XHR are still in use.
So, these are carrying the dependencies from SDK3's web, and… And all the resources, and so on.
Trent Mick 00:17:32 So, I guess, okay, so I would say we cannot yet drop.
instrumentation, fetch, and XHR, probably, right? Because if we only, like, deprecate.
David Luna Bistuer 00:17:44 Knowledge.
Trent Mick 00:17:45 Or haven't even defecated them yet.
Then we probably need to keep them. Okay. Yeah. Then… either… if they depend on SK TraceWeb, some of the utils in there, either we move those utils into the instrumentations.
and drop SDK TraceWeb.
Or we keep SDK TraceWeb going for another round.
Here, I don't… I don't have an opinion either way yet.
Marc Pichler (Dynatrace) 00:18:11 One of the options that we have with dropping these packages is also to just drop it in the middle of 3.x.
Trent Mick 00:18:20 Yep.
Marc Pichler (Dynatrace) 00:18:22 We just need to figure out… yeah, we need to figure out a way to, issue… bug fixes.
And… Stuff like that.
To the package then, because we're essentially committing for another Year of support.
So that's something we'd have to look into.
Trent Mick 00:18:48 Okay.
Marc Pichler (Dynatrace) 00:18:49 That's CCD.
Yeah, since it is actually just re-exporting what we have already in, SDK Trace, we could also just put a caret dependency on it.
Or move it over to peer dependency, which is somewhat annoying, but, Or let me produce which SDK trace version to use in the background.
Or we could, strip out the whole tracer provider thing, and rename the package to WebTuters, or something like that.
I guess what I'm saying is there's multiple options to do it later, if we have to.
The cleanest solution would be to just… Do it now.
Trent Mick 00:19:50 Can we…
David Luna Bistuer 00:19:53 Okay.
Trent Mick 00:19:54 get SDK Trace Web to no longer need SDK Trace Base?
Marc Pichler (Dynatrace) 00:20:00 Yes, we can. I think so. Because what these instrumentation users are doing is… they're just using the API to… set things. I don't think there's any reason why they would need to be in the SDK package.
Trent Mick 00:20:21 the… the SK TraceWeb also has… so, instrumentation utils is one big thing, but just looking again, it has this… it has a web tracer provider.
Marc Pichler (Dynatrace) 00:20:31 Yeah, I think the…
Trent Mick 00:20:32 that.
Maybe it doesn't do anything special.
Marc Pichler (Dynatrace) 00:20:36 I think it just had this register, but it… I dropped it in 2.0, if I recall correctly.
Trent Mick 00:20:43 And it has the stack context manager.
Or which there's an equivalent in the new browser SDK, so I guess people could be pointed there.
But maybe none of that requires… the… SDK trace base.
I guess, yeah, what I'm driving at is let's keep SK Trace Web, there's a proposal, but make it not depend on SK Trace Base anymore, so that we can drop SK Trace Base.
And then we can drop SK Trace Node, because we've already deprecated there.
Okay.
Marc Pichler (Dynatrace) 00:21:18 Yeah, I think that's a good idea.
Trent Mick 00:21:20 Okay.
Marc Pichler (Dynatrace) 00:21:21 And…
Trent Mick 00:21:21 Try not.
Marc Pichler (Dynatrace) 00:21:21 If it happens that we, can also drop the UTERS, then even better, then we don't need to do all of that.
Okay.
Trent Mick 00:21:29 Yeah, we…
Marc Pichler (Dynatrace) 00:21:30 and…
Trent Mick 00:21:30 out SDK Trace Web as much as possible. Yeah.
David Luna Bistuer 00:21:36 a quick check, maybe it's a long shot, but these instrumentations are actually just importing utils from the SDK trace web. They don't… and those utils do not depend on Any other SIG buckets?
So maybe, okay, maybe it's just juggling a little bit, but there is this webcommon.
Packets that we have.
That actually already contain some mutals, so if we can extract them to there, then we can just, you know, make these instrumentations free from any SDK package.
Trent Mick 00:22:07 I would be… But that webcommon… wait, is that webcommon in the… In the core repo?
David Luna Bistuer 00:22:14 Yeah.
Oh, okay.
Marc Pichler (Dynatrace) 00:22:18 I think it would essentially just end up being the same problem that we had with SDK Trace Web, where then instrumentations depend on an SDK package.
But… Yeah, it… Wouldn't make things any worse than they are currently, so…
David Luna Bistuer 00:22:42 Well, the point would be that, people with the… they can use the new SDK and browser, but they can't just, you know, use the former FETS instrumentation.
Marc Pichler (Dynatrace) 00:22:52 Absolutely.
David Luna Bistuer 00:22:53 If they still want to, and they're not pulling another, you know, copy of the SDK TraceWeb.
Marc Pichler (Dynatrace) 00:22:59 Yeah, that makes sense.
Yeah, so it does actually make things slightly better, yeah. You're right.
David Luna Bistuer 00:23:05 Yeah.
So, yeah, so people, if people are not feeling comfortable with this experimental instrumentations in browser, they can still use the formula once because they come from TD API, but they are not pulling any SDK code. The SDK is probably the SDK, and then the instrumentation is just, you know, the instrumentation itself, and the webcommon that contains some URLs.
And if the bundler is smart enough, maybe if they're using both instrumentations, they can recheck or share the… dependencies of this, on these utils. I have a look, and maybe I'll put a comment here in the issue.
So if it's doable, and tomorrow, we'll also check with the project folks.
Marc Pichler (Dynatrace) 00:23:46 Perfect, thank you.
Right.
I guess, let's go over the other ones, then, quickly.
I actually haven't read into that one for a while now.
Trent Mick 00:24:14 Oh, this is mostly about the environment handling, and then any other configuration stuff is… I think probably well in hand with the declarative config work.
Yeah.
Marc Pichler (Dynatrace) 00:24:24 So we probably would need to split that up into concrete action items for 3.0, I guess.
Trent Mick 00:24:31 I think we have other issues that kind of cover it.
Marc Pichler (Dynatrace) 00:24:35 our… Wouldn't need refinement on that one.
So that we can see if… if there's anything missing, otherwise we'll just close that.
And refer to the declarative config work, and… the pre-existing issues that we have for removing the MFAR configuration from the direct packages.
Trent Mick 00:25:02 As a… I'm gonna Hi, Jack, the threat as a… that's a convenient reminder that that issue is currently the blocker on moving forward on… And Vend declarative config-based stuff. That's the big one where… Marilla and I have a… Different design opinion.
Any reviews on that would be welcome.
Marc Pichler (Dynatrace) 00:25:39 Probably put a link somewhere, right?
Trent Mick 00:25:43 Sure, I can edit for that.
Just here.
Marc Pichler (Dynatrace) 00:25:57 That's the one that we talked about last week.
It's step one, right?
Trent Mick 00:26:18 I added a… agenda item for it, but we'll just pass over, and it's just a request for reviews.
Marc Pichler (Dynatrace) 00:26:27 Alright.
I think this one was, leftover from…
Trent Mick 00:26:42 Oh, from a long time ago.
Marc Pichler (Dynatrace) 00:26:43 Yeah, this is the main issue that we have with pure dependencies. I think what we landed on was that this is not something that we can easily do without actually introducing an API major version. So I'm not sure if this is… Right.
To have in the current milestone.
I would remove this one for now, because it's out of scope, I would say.
Trent Mick 00:27:16 Agreed.
Marc Pichler (Dynatrace) 00:27:26 Alright, and this one be… Also had talked about, more or less, with the removal of, the SDK trace web package, or, like, moving the utils, at least, and deprecating them.
So I guess an issue exists, and We also put the needs refinement on this one, so that we link everything together, and we can either close this, or the concrete one, or keep it open until the stuff is done.
This one, I think we haven't talked about yet, I was just looking over the context zone package, and I was, seeing this ever-growing list of, ZoomJS dependencies that we support, and I was thinking of dropping some of these.
Any objections to dropping the older ones?
I guess we can just leave that, like this… there's still quite a lot of users, even though the web SDK will be without Zoom.js, there's still a lot of people that use that context manager, so I guess… we would still keep it around for 3D, though, at least.
Trent Mick 00:29:07 Is that gonna force us into some… painful thing with old versions of and that kind of thing. I don't really know what the implications are.
keeping it.
Marc Pichler (Dynatrace) 00:29:21 I'm also not sure, like, the old versions, like, it hasn't really… given us any headache, I would say. I have never really run into a person that, reported a pack that was just… they are on an old, Zoom.js version or not.
It's really just the fact that we don't test for the old versions that's the issue. Where if somebody makes a change, we can't really see easily that, something breaks, because they're using a newer feature or something like that.
Trent Mick 00:30:10 Wow, there was a Zone.js release in… May.
It's alive.
Marc Pichler (Dynatrace) 00:30:24 Alright, moving on to the minimum supported Node.js version, We had a bunch of discussion here, and like, after… This suggestion here, we… essentially decided on pushing the 3.0 release to the end of September, which is what we're doing now.
I would say to… best version range that I've seen is, this suggestion here, so, I'd be okay with… Moving on to that, version range here.
Trent Mick 00:31:05 Yeah, I think we can… we'll maybe refine that a bit, but that can be our minimum.
I'm not even sure if we'll refer to 23, I think that's out of support as well.
Marc Pichler (Dynatrace) 00:31:15 Yeah, I think what we are saying in the README is that we support, current and maintenance RTS versions.
Trent Mick 00:31:23 Yeah.
So it'll be some version of 22.
As the base, but we can… Possibly go a higher minor than that one.
Marc Pichler (Dynatrace) 00:31:34 Yeah, agreed.
Do we want to split that off into a separate issue? That is mostly the discussion here, and actually making the change should be fairly simple.
Trent Mick 00:31:50 Sorry, do you think we need a separate issue, or just…
Marc Pichler (Dynatrace) 00:31:52 We don't need to… For an upcoming would probably suffice.
Trent Mick 00:31:58 Yeah, I think we can just follow up. I can… I'll get there at some point.
Marc Pichler (Dynatrace) 00:32:03 Thank you.
Alright, so there's that. Async hooks Context Manager is already deprecated, so,
Trent Mick 00:32:22 Yeah, that's easy, I think we'll just do it.
Marc Pichler (Dynatrace) 00:32:29 I had this idea of actually renaming the package, but I think that would just, introduce more churn than necessary.
I will put a comment here to say that, we can just remove the async hooks context manager and keep the package name as is.
Does that sound okay?
Trent Mick 00:32:52 Yeah, I think so.
Marc Pichler (Dynatrace) 00:33:04 Let's, do that right now. So we get.
And, remove the needs refinement.
Oh, man.
Oops.
Like, removing that is, fairly easy.
Doesn't need too many details.
Actually, since that list is fairly long, should we… Hop onto some of the other topics first, and then continue with the… Through the Marstone stuff.
Trent Mick 00:34:09 That's fair.
Marc Pichler (Dynatrace) 00:34:11 Alright, and let's pause that for now and move on to the… widening attributes plan here.
Trent Mick 00:34:22 Okay, so my assumption would be, and I'm glad to hear if they're different opinions, is that as part of 3.0, we would try to also do the… logs… API and SDK GA.
This month, or is that not the case?
Marc Pichler (Dynatrace) 00:34:38 I think we would still need a TC review, which might take some time. So I would actually defer that to after… 3 to all.
Trent Mick 00:34:50 Except that we did want to make changes that would… Okay, so this one in particular is the major, I think, remaining issue. Modulo, I haven't really looked at the other.
few issues that are on the milestone as well, and then TC review.
That… at least this proposal was widening the attributes type in the API, which will be a breaking change for SDK implementers, so there's… I don't know if that counts the same as a breaking change for the SDK.
I guess it doesn't… it could happen in the 3… Duto, because… Actually, I don't know.
I need to think through that.
Marc Pichler (Dynatrace) 00:35:32 Actually, what we can do is… so… I merged a few PRs to add pre-release support to our whole, release pipeline thing.
We could merge this, and do an API pre-release, which is currently not allowed by my, like, extensive checks to make sure we don't publish anything that we don't intend to. But we can just remove that check and also do API pre-releases in that case. So we release API 1.10, development.
Preview.
And we actually see if anything breaks.
We can test it out.
in various locations.
You can test it out in Quantrip and see if anything breaks.
And if we're confident, we actually ship it with 3.0, and then we're one step closer to actually getting the trace, the logs SDK Stable, because we have that dependency cleared out.
Trent Mick 00:36:47 Okay, on… on… Okay, that sounds… Good.
on the getting TCU review for this, Carlos, I notice you're on the call, are you able to… speak to.
What remains there, if anything?
Carlos Alberto Cortez 00:37:02 Yeah, actually, I would like to review, first one, this VerdiPR. I know it's draft, but I would like to review this, and And from there, we can take it. Yeah, I think that before I forget that, I will do… I will review this before the end of the day, and provide some feedback.
We can discuss.
Trent Mick 00:37:18 Sure, okay, well, let me… let me briefly describe what this PR is about. So, there'd been an earlier PR that I'd done to… change the… type of… attributes, in the API to be a union of exactly the Types that are allowed in the spec for any value.
Back in June… Dan, another maintainer, had suggested… trying, the… a different type, or so use the TypeScript type unknown, which basically means wide.
an unspecified type. What it basically would mean doing that, and that's what this PR has started doing, is that any of the APIs that accept attributes or anywhere any value is accepted. Basically, you can pass in anything, and it's up to the SDK implementation to… defensively, handle… Anything being passed in.
to a certain degree, APIs Some APIs in the SDK, so, for example, span attributes, where those are accepted, were already defensively limiting and dropping attributes that were of unsupported types.
And RuntimeJS, which isn't TypeScript anymore, is, of course, untyped, so really a resilient SDK already needed to be handling whatever garbage the user passed in.
so, there's some arguments to be made there that SK's already kind of had to be doing this. There's some… some subtlety on TypeScript handling and whether anyone was using the attributes type and doing a thing in TypeScript called, Type narrowing, which can run into… This is where we talk about whether it's a breaking change or not.
The… work that I haven't done in draft here, and I could show some, is playing on… ensuring or testing what happens when super weird things are passed in for attributes. So, functions or arrays that have symbols in them, or… Anyway, a bunch of edge cases and circular references, that kind of thing, and testing to see whether our SDK implementations at least handle all those cases. Right now, it's… the current state is kind of weird, and users of the JS API can pass in anything already, so some of this is going to be Handling bugs that basically already exist and aren't tied to this one.
But, okay, so from the logs SDK and API point of view.
Most of this code that we're talking about is close to what… the current logs API and STA implementation already do, and that the attributes type, it has its own log attributes type.
Which was the wider… thing. That one was the, defined as the union of allowed types, so not quite as wide as this unknown thing. So there is a little bit of an impact to reviewing the API and SDK. Another would be a bit of a change. But, ignoring that little subtlety, mostly this is about dropping the logs API, having its own special types for these things, because those types will exist in the shared common API, and just using those. So instead of log attributes, it's just using attributes, because that attribute now supports the complex types that the logs API needed.
If that helps.
Carlos Alberto Cortez 00:40:53 Yeah, definitely. And I guess that, in that regard, if I understood correctly, Mark, what you're saying is that there not be enough time for a review of the API, which uses this new wide type.
Right?
Marc Pichler (Dynatrace) 00:41:11 No, I was, so we're on… quite a tight schedule with, SDK 3.0, though. And what I was referring to was, getting the TC review for the logs SDK done.
Carlos Alberto Cortez 00:41:27 Right, right.
Marc Pichler (Dynatrace) 00:41:28 Oh, yeah.
Carlos Alberto Cortez 00:41:29 Yeah, I don't know Yeah, my… okay, sorry, go ahead, you go first.
Marc Pichler (Dynatrace) 00:41:34 So, yeah, the… My main concern is that we just end up with a bunch of action items for the logs SDK and work through that, even though that could be done in a minor release after we got 3.0 out already.
So it would land in 3.1 or something like that.
Carlos Alberto Cortez 00:41:58 Okay, because what Trent was explaining, I think this one could make sense to be review and merge, if possible, before… The first 3.0 version goes.
Marc Pichler (Dynatrace) 00:42:09 Yeah, exactly. Since this goes into the API, and we now have, we're gonna cut pre-releases, like, ideally multiple times a week, to get people to try stuff out. We can… Be a bit more brave in merging this, and let people… Try stuff before actually… Labeling it as a production-ready release.
Carlos Alberto Cortez 00:42:37 Also, on your… on the point of that… to your point, Trent about the box and SQL references and that kind of stuff, I think that their existing implementation, we can go and check how they did that, and… Yeah, but if you are confident that this widening is fine, I think we, as you said before, like, the SDK is already checking in case a user is providing garbage, so that's a good thing.
Trent Mick 00:43:04 some parts of the SDK are. So, but I mean, I'm saying, like, I'm not sure that the type widening makes this resilience of an SDK implementation any worse. It's just… this is an opportunity to go realize and deal with those cases.
Carlos Alberto Cortez 00:43:20 Yeah.
Okay, so I guess that there's still value, right? If I review this one, Trent?
Trent Mick 00:43:27 I think so, yeah, and then from your point of view, is there much more that needs to be done for review? I don't… like, this is my first time, so…
Carlos Alberto Cortez 00:43:34 For the login part, or just the one?
Trent Mick 00:43:36 For the… for the logging, yeah, for us to be able to get approval to follow GA.
Carlos Alberto Cortez 00:43:41 We can try to get… I can erase that and to see, like, I think Jack one… what's interesting, Jack from Java, who, you know, who also has experience implementing the widening of attributes, so we can see whether he or somebody else has time. I already, as you may remember, I did a quick pass.
It… yeah.
Trent Mick 00:44:03 Yeah, you opened some issues, and I think Mark mostly dealt with them, yeah.
Carlos Alberto Cortez 00:44:06 Yeah, so I think that getting somebody, To prepare, you know, a second look could be useful.
Not super, like, necessary, but useful, you know?
Trent Mick 00:44:19 Right, okay.
Carlos Alberto Cortez 00:44:21 So, yeah, okay, so let me ask, let's see, hopefully we have somebody. If not, there are people, like… could be… well, I'm not sure how that would work, but there are people who are, like, experts in logging, like Robert Payac from the Golang SIG, and he could, like, kind of, on behalf of the specification group, provide a second review for… even if the TC is busy now, for example, you know?
Trent Mick 00:44:46 If he's able, that'd be… that'd be great, yeah.
Carlos Alberto Cortez 00:44:48 Yeah, yeah, yeah. So, I mean, it depends on, like, the cycles and all that, but yeah, I can ask away. So, let me ask that today, so there's a realistic expectation of how things are going here.
There's… yeah, let's talk offline a little bit. I think that, for example, like, the package organization was nothing that didn't come to me obvious.
the first time I was reading this, And this kind of stuff could be nice for somebody reviewing this. But otherwise, in my opinion, it's looking good. So, okay, so, follow-ups. First, I reviewed this PR of yours, Trent. Second, I ask away, for whoever would be interested in doing a second review.
Trent Mick 00:45:31 Yes.
Carlos Alberto Cortez 00:45:31 As soon as possible, yeah.
Trent Mick 00:45:33 Yeah.
Yes, and thank you.
Carlos Alberto Cortez 00:45:36 Okay, thank you.
Marc Pichler (Dynatrace) 00:45:40 Thank you.
So, I guess we landed on… If we can make it happen, we'll make it happen.
And… I'm gonna look into the API pre-release.
Possibilities, you know, that we can… Test things out, outside of our own repo.
And we'll go from there.
So that was this one here.
Then we have… another topic by trend, this is the PR.
Or the configuration package changes.
Guess this is a car for reviews.
Trent Mick 00:46:38 Yes, that's it, yeah.
Marc Pichler (Dynatrace) 00:46:42 I did not have a lot of time to look into this one, but, Hoping to get around to this soonish.
Maria will also be…
Trent Mick 00:46:58 He's away this week, so…
Marc Pichler (Dynatrace) 00:46:59 Yeah, so… Alright.
Is there any, particular question?
Or comment about this? Anyone?
If not, then, we can move on to the next topic here by, so, yeah… About the instrumentation anthropic package.
Surya Teja 00:47:37 Hey, just a quick, request for, review.
Nothing more.
Marc Pichler (Dynatrace) 00:47:46 Alright, thanks. Yeah. Unfortunately, I'm, kind of busy with the… redo their work, but if I find some time in between, I will have a look at that.
Otherwise, if you can… find some approvers who are willing to have a look at, or would be happy to defer the review to them. Usually, a maintainer reviews addition of new packages, but, I'm also fine if a reviewer take… or an approver takes Over looking into this one, and once it's approved, I'm… I think.
I'd be ready to just merge this one.
Surya Teja 00:48:31 Can I work with Jackson? I have been working with, Jackson… Yes.
Marc Pichler (Dynatrace) 00:48:40 That sounds… sounds good, yeah. Jackson is an approver, I think, so… yeah. So… that's perfect.
than, you know… once it's approved, let me know, and I'll merge it in. I'll give another, review, just making sure that all the package versions are in order and stuff like that, to make sure nothing breaks during the release, but, yeah, sounds good.
Trent Mick 00:49:06 Is this associated with, or does it overlap with the open inference?
Surya Teja 00:49:11 This overlaps with… Yeah, this overlaps with open inference, yeah.
Trent Mick 00:49:21 Okay.
Marc Pichler (Dynatrace) 00:49:22 It's part of the open inference donation, if I understand correctly, right?
Surya Teja 00:49:27 Yes, yes. So, there are two path tracks. One is a common utilization AI that Pranav has been developing, and this is adding the packages and steps that Open Inference has donated, so that once that utilization AI is ready, We can use that, and… Capture the common inference agent and other spans.
Marc Pichler (Dynatrace) 00:49:52 Yep, August.
Trent Mick 00:49:53 Yeah, I just, I, yep, I finally see the reference.
Surya Teja 00:50:01 Yeah, I don't know if, this has been discussed or not, but if you could enable stacked PRs, that would be great, because these are quite huge.
if I can break them into smaller PRs, that would be helpful for the reviewers, and I can group everything together so that You can have an end-to-end picture when it's ready for a review.
Marc Pichler (Dynatrace) 00:50:28 Yeah, we discussed it earlier, the summary is we would like to, but we'll have to look into, some security considerations to allowing people to push to the, To the repo itself, instead of doing it from a fork, because right now it's not available.
Surya Teja 00:50:48 Yeah.
Marc Pichler (Dynatrace) 00:50:49 works. So, we'll look into that, and We are also interested in enabling that, so hoping to get that done soon.
Surya Teja 00:51:00 Yeah, no rush, because on the GenAI side, too, there are other things that we have to sort out.
But just calling it out.
But thanks a lot for responding positively.
Marc Pichler (Dynatrace) 00:51:13 Alright.
Yeah, I guess I'm gonna hijack what I've been talking about the, About the open inference donation there.
I had a look at this issue here, and was wondering if we are going to, like, actually take in all of these, or if we can skip some of these. The one that stuck out to me was this Langchain V0 instrumentation, which says legacy here. If possible, I'd like to skip that.
Because it also doesn't seem to have that many reviews here.
Surya Teja 00:51:59 So, if… let me understand the question correctly, and then I'll give you an answer. You guys have a lan chain, instrumentation, and that's in a functional state, I believe. Did I understand this correctly?
Marc Pichler (Dynatrace) 00:52:12 No, I think.
Trent Mick 00:52:13 Not functional state. It's just a skeleton that's… Plugged in and not… or that's committed, but not being published right now.
Marc Pichler (Dynatrace) 00:52:20 Yeah, so what I was referring to is, there's instrumentation langchain here.
That's being donated, which has a lot of downloads, and then we have another instrumentation, Langchain that's being donated, which is for V0.
something of langchain.
And that's the legacy instrumentation, and I would like to… Not merge this one.
I only merge this one to make sure that we don't end up with an old package that we have to maintain going forward.
Which provides little value to folks, because… It already has very few downloads, so… wouldn't be worth the effort.
Surya Teja 00:53:12 Yeah, I agree on that. We were not planning to add V0, and initially I thought that Langchain is already covered by your instrumentation, but yeah, I'll take a look over there. This is something new to me.
Marc Pichler (Dynatrace) 00:53:27 Yeah, unfortunately, I think we merged it, just the package skeleton without any code in it. So it's just sitting there waiting for somebody to come along and add code to it.
from… So, would be nice, if… Anyone's interested in doing that, then we can also get that off the ground.
Surya Teja 00:53:49 Yeah, we got some interest from Snowflake folks.
In helping over there. Currently, Python is at a phase where we are going to soon wrap up. If we can find some more folks who are well-versed with JavaScript ecosystem, we can jump on this and help you guys with adding these donations, but For now, we are concentrating only on Frontier Labs, like Anthropic and OpenAI, and get to a place where we have instrumentation for those, and then incrementally add the other stuff, like Llama Index, Lansion, and others, which are having huge community.
Interest, but… It's going to… we are there for, helping, and we would love to… Do it in such a way that we are not going to… disruptive.
Trent Mick 00:54:42 is… crazy ideas. I don't expect to get an answer here, but Python did… Create a separate repo.
for GenAI instrumentation work, presumably because they could move faster there. I don't know if it's a similar kind of thing, if we end up being a review bottleneck.
Is it worth having a separate group there that has a different setter?
Reviewers, rather than… I don't know. Me feeling guilty, because I can't spend any time on the GenAI instrumentation reviews and ending up being indirectly a blocker of the stuff going in.
That's one angle. Another angle I can think of is… is the GenAI instrumentations can be huge, and maybe… dealing with, like, one shared package log file in the JSQRIBR repo.
Can be easier if you separate that out.
to a separate repo, so, I don't know. I assume a… Other people have thoughts.
Surya Teja 00:55:44 Yeah. Question before we split out Python was we had some shared Python country jobs and everything that we could reuse, and it took a little bit of effort from the Python country, maintainers or stuff to help us get that onboard.
Are you guys having that bandwidth?
For helping us to spin out a separate repo.
And, help us over there.
Marc Pichler (Dynatrace) 00:56:14 I think spinning off a separate repo wouldn't be that much of an issue, because… Like, the workflows themselves, they're… like, not super complex, I would say. Like, they have grown to be complex, but, like, they should cover all the things, that we're seeing in the country repo, which also means they should cover all the things that we're seeing with GenAI. It would be just a matter of copying the workflows over.
But getting it off the ground and requesting a repo, getting the repo set up, creating a new maintainers group and stuff like that might take a long time.
So…
Trent Mick 00:57:03 Yeah, I don't know.
Easy for me to say, because I know Mark's done most of that.
Kind of.
the… Coordination works, so… I don't, I don't know if it would.
Surya Teja 00:57:14 I don't…
Marc Pichler (Dynatrace) 00:57:15 I'm not too opposed, to actually having that. I think at some point, we will have to think about federating the, Contra people.
Because there's just so many packages in there, and it might be… Easier for folks to go to the… GenAI repo, and… contribute there, if that's what they're interested in, and then go to a, I don't know, database.
Ripple, and, contribute there, and, like, have a shared A shared overarching topic.
So a similar split to what's being proposed in… in SEMConf.
Makes sense, I think.
But for that, we would have to figure out how to distribute these packages, which…
Trent Mick 00:58:15 What do you mean?
Marc Pichler (Dynatrace) 00:58:15 Look.
Trent Mick 00:58:15 You're talking about the auto-instrumentation snow problem, or…
Marc Pichler (Dynatrace) 00:58:18 Yeah, the auto-instrumentation's no problem. And having some way to also published that.
with either the GenAI stuff enabled, or, like, a separate way to just add different packages.
To your app.
To get it instrumented.
Lots of unknowns there.
In that regard.
I guess we won't be done just hosting the packages somewhere else, we'll also need to figure out distribution of packages.
Trent Mick 00:59:01 Well, so distribution would still be publishing, too.
at OpenTelemetry on NPM.
Marc Pichler (Dynatrace) 00:59:07 Probably, yeah. And then we end up with more folks that need to have access to it, or…
Trent Mick 00:59:13 Potentially, yeah, or if… yeah, yeah, yeah, I see what you mean.
Marc Pichler (Dynatrace) 00:59:17 So, yeah.
Trent Mick 00:59:18 Yeah, that's where… that's where I'm not sure does it help, or does it.
In the end, it's caused more work, yeah.
Surya, what's the… on the Python Gen AI repo, is it a totally different set of maintainers and approvers? Or is it… is there an overlap with the core Python… A telfo Current.
Surya Teja 00:59:40 We have some core overlap with the, maintainers. But we also got few others who contributed to be the maintainers so that they can help reduce the burden.
Right now, Vladmilla is running the show over there, mostly, because, The contributions are… You know, she's running the show over there.
But a few Python Books folks supported her in the initial stage.
I can, start a conversation in Gen AI group, because initially.
we thought of having a separate JavaScript repo, but we were not sure if, What to do over there, since, we are swamped with Python. If you guys can help, and if you're… if you think that that is the best path forward.
We can start a conversation there and see if folks can pitch in and help you guys to alleviate some load on your side.
Trent Mick 01:00:46 Yeah, I think it's premature to say we decided we're going to do that. I just wanted to throw it out for early discussion, so I think we should just… Let it sit for now and see if… we get to a point where it's feeling so painful in Contrib that we want to consider a separate repo, but yeah.
Surya Teja 01:01:07 Yes, we are…
Trent Mick 01:01:09 Over time now. Yeah, thank you.
Marc Pichler (Dynatrace) 01:01:10 We're over time now, so, let's continue discussing next week.
Or we can also start a thread in the select channel.
And continue from there.
Alright then, thank you everybody for joining, have a nice week, and see you next week.
Jackson Weber 01:01:29 Okay, have a good one, y'all.
Hector Hernandez 01:01:31 Thank you.
