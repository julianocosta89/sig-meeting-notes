SIG: Browser SIG
Date: 2025-08-21
Duration: 32 minutes
Zoom Recording URL: https://zoom.us/rec/share/fbq7fd_mDymTL2s4hfgolM4W0V7fLeXVK_l30E8ulGkjMUKmZHBQMcATbiRIvtiG.zb6SJfwxk_a_AhdN
============================================================

## Zoom Recording Transcript

**Jared Freeze (embrace)** 00:46 Hey, Thomas.
**Thomas Hunter II (Datadog)** 00:47 How's it going?
**Jared Freeze (embrace)** 02:51 So, I know Ted's out. I was waiting on Martin to join.
She had some thoughts on Slack, but….
**Joaquín Díaz** 03:50 How do we get started?
**Daniel Dyla (Dynatrace)** 03:55 Nobody knows what to do without Ted.
It looks like, Joaquin, you had the first, item here. This is the same…
RUM use cases document that you showed off before, right? Oh, no, it's not. Okay.
**Joaquín Díaz** 04:09 No. No, it's actually, … so, I don't need to show it here, I think you can read offline. …
But what I did is…
I remove all the challenge reports, and I focus on the data that we want to capture. So, I didn't want the composition to be around, like.
How the data is going to be sent.
Like, whether it's events, spans, or which attributes, whatever.
I just want to mostly talk about the information that, we all think is useful for users to have.
And maybe some, like, examples on, like, which ROSA API to use to capture that information.
But yeah, I think my idea would be that
Once we all agree that that's useful for users, we can then…
split the work, and maybe start thinking out how we are actually going to track, like, which telemetry we're going to create, and how we're going to send it, and, like, which attributes, and all that.
But I think… first, I think we should agree on, like, if this is the right information.
So that is what I only wrote about that on that document, so yeah, feel free to take a look.
maybe we… I just shared yesterday, so I know it's not a lot of time, so maybe we can, …
Talk about that next week.
But yeah, first, if you had any feedback, I appreciate, Martin, and I think they… David, yeah, David was… you were already adding some comments, so that's great. So thank you.
Yeah, we can maybe…
fantastic discussion next week, and start breaking it down into smaller pieces that we can work through.
**Martin Kuba** 05:56 Yeah, thanks for doing that work, Joaquin.
I think it's… it's… Aligns, like, with what we've…
Had worked in before as well, and there's, like, some…
So I think it very much aligns with, … Yeah.
**Joaquín Díaz** 06:18 Yep, I agree.
**Daniel Dyla (Dynatrace)** 06:21 Looks like you also have the second item here, talk about the possibility of having a new repo.
**Joaquín Díaz** 06:28 Yeah, I think we discussed this previously, it's been raised again, recently.
In my opinion, it would be better to have a new repo. I also recently shared
The test contrast repo is just a well-be-used subject base, pretty much.
But I think, like, overall, everything should be simpler if we can have one repo. I know
there is a lot of shared code between Node and the browser, but there is a lot of difference as well that add to the complexity of having one shared repo.
I think the main concern will be how do we use what we already have, and I agree that we shouldn't be writing, like, code again that already exists?
So, initially, I would say, like.
Everything can be by dependency of this new repo, everything that we already have.
And we can start by just having what we don't have, which is
Of course, going to be browser-oriented and not-oriented.
And then eventually.
As we see things that are more complex to maintain in both, or in JS, unlike, you know, all the…
things that are, like, connected with null , but not really. Like, for example, I've seen the fetches invitation, it has an if that says, if this is null , do nothing, and stuff like that.
That just adds complexity to the call. …
Yeah, and we also discussed about, like, TS configs, like, linter config, PDR config, and everything.
That is easier if it's only sync it on, the browser environment, and no, no.
… but yeah.
Curious with.
Get your thoughts on that.
**Daniel Dyla (Dynatrace)** 08:16 Is this based… have you actually run into any concrete problems, or is this just something you think…
Might, like, give an example.
**Joaquín Díaz** 08:27 I don't think…
we've run into any trouble yet. I don't think… I will say, like, technically, I don't think it's impossible to… everything to live in where we go.
I'm just saying it's easier for everyone, but at least in my opinion.
… That is working on the repo, do not worry about null .
But, yeah, technically, yeah, we can't have one repo, for sure.
… That's what I take.
I know. I think… yeah, I think you were looking at some stuff that you were trying to work on, and you had some issues.
Right?
But it was, I don't know if it felt maybe out of date, or….
**Jared Freeze (embrace)** 09:08 Yeah, so I was… I was just trying to get familiar with the contrib repo, and looking through it, you know, it'd be really nice to have a rule that's, like, no built-ins.
Right, for web, in ESLint. And you basically have to call out, like, every folder in that config to control it, or…
put the ESLint config in that folder, right? Like, as a package.
it's not a… it's not a huge problem, but, like, if you're gonna use NX or Lerna at the top level, you know, their new… the new world is, you know, use a single config at the top, don't import
you know, down below. I know it's still possible, but it's not recommended. So, if you do have, like, a single root config where it's a true monorepo, then you're gonna need rules in there that are, like, calling out the packages that are Node and the packages that are web.
And I was… all I was saying was, like, it just feels like a lot of management. So, a new repo is also a huge step.
To have, you know, to be moving stuff and keep things in sync or whatever, but, you know, just, I was thinking about CI as well, right? Like, yes, you can only run…
certain tests on certain folders if web changes, but, you know, you have this dependency tree that's… I think it gets more complicated, pretty quick. So, you know, one of the things, too, in the test harness is, like.
You know, run the browser suite.
you know, run the hotel browser suite on, like, Next, right? And there's a whole browser test, like, I feel like there's gonna be parts… some of the node parts that, like, you know, they're not gonna wanna wait for that. So, somebody… somebody commented…
That they're working on speeding that up.
Which is good, but it just…
it kind of seemed like independence might be a good thing here, so… I don't know how everyone else feels, but, it would…
be nice to centralize. Again, I know there's cons as well, right? Like, being out of sync with the other main repos, potentially, or… you know, I know there's scripts that, like, does versioning across packages, like, we'd have to replicate those things, so…
Yeah, I'm curious what everyone else thinks.
**Martin Kuba** 11:27 And I also wanted to ask, and I added… we talked about this in Slack a little bit, but in addition to
These kinds of stuff.
There's also, like, we have documentation that we need to figure out where to put it.
So the options would be, like, either put it, like, in a new repo, or put it, like, find some place in the semantic conventions.
that's specific for client, or maybe, like, in the JSQ contrib, …
So, like, with, with, like, the… with, like, this…
like, the linting and, like, this kind of the tooling around, like, the test harness documentation. …
like, if we have it kind of spread out across, like, many different repos, like, we felt like it would be easier also for us and for users, like, to have it just all in one place.
And I think, you know.
users, let me know, I'm also curious, like, what people think. Like, when users know.
want to know, like, what, you know, what to do with, how to use Autel for browser, like, where do they go? Like, it's not…
It's not, like, really clear, so, like, this would, like, make it very clear.
**Jared Freeze (embrace)** 12:42 Yeah, I do like that. You know, making it easier to adopt, I think, is gonna be key here, right? So….
**Joaquín Díaz** 12:59 Right, but we want to take…
Collect all our thoughts in one place.
However, I'll take a look.
Or, like, I don't know how we can continue this conversation.
It doesn't look like we have a… figure out.
an option selected already, so I don't know.
**Jared Freeze (embrace)** 13:20 Yeah, we can just make a Google Doc, like, pros and cons.
… That's easy. I mean, I have some thoughts on that, and then people can just comment or whatever.
Yeah, let's… let's do that. And I'll… I guess I'll just link it to… the SIG meeting doc.
**Joaquín Díaz** 13:38 Okay.
**Martin Kuba** 13:45 Daniel, are you strongly opposed to this, or Mark or Daniel?
**Daniel Dyla (Dynatrace)** 13:50 No.
I think from… my perspective, the… the JS… … repo…
It… it is complicated by the fact that we have web and Node.
Stuff in there.
Unfortunately, splitting stuff into a separate repo probably doesn't remove a lot of that complexity for us, because we still have to test all the SDK components, we still have to run all the browser tests and stuff like that, so… doesn't really reduce complexity for us.
But I could see how it would reduce complexity for, for the browser folks.
The main…
concern that I would have… there's a couple of things. One is that the SDK, like, versioning has been a total nightmare in the past, and having it split across multiple repos is only going to make that worse.
Right now, we have the version numbers locked together, for all… all stable packages have the same version number. All experimental packages have the same version number.
And we still have people that, try to mix and match the wrong versions all the time. I think Mark deals with that more than I do, so maybe he can chime in there. But, I foresee that becoming a bigger problem, not a smaller problem.
… the other… like, I guess just from, like, a process perspective, if…
I want to avoid the situation where…
Something gets implemented in a browser-specific
Repo, that would be beneficial for everyone, because for whatever reason, somebody's either used to working in that repo, or thinks that, like.
it'll just be faster if I just put it here, or whatever, and then work is duplicated.
…
Those are probably my two main concerns. The second one is fairly easy to rectify, as long as you have a set of disciplined maintainers that can recognize when things are, …
I trust that that's not a difficult problem to solve. The first one, I think, is a difficult technical problem. You'll end up with users that are confused by different version numbers.
**Joaquín Díaz** 16:16 Yeah. So maybe….
**Daniel Dyla (Dynatrace)** 16:20 Go ahead.
**Joaquín Díaz** 16:22 But, yeah, for the second one, I think, like, …
I think we should define that if there is something that is shared across node and the browser, we should define where it should live.
It seems to be the answer should be the JS repo, because there is already some stuff there that is going to be shared.
But yeah, as you said, we have to be disciplined about, like, making sure nobody's committing code that can be shared in the web repo, probably.
… For the first one, I was thinking, like.
for users, if it is complicated to understand the versioning, like, I don't know how hard it would be, but I'm sure we have to think about it.
But… If all, like…
if the internal dependencies are dependencies for the browser repo, and then as a user, I only have to install the web repo, right? So I say.
NVM install, like, open chemistry browser, a version 1 browser, right? So that should take care internally of getting the right, versions internally that are the ones that are conflicting.
And then for the user, it's just one version. …
that at least will fix some of the issues. You'll still have issues a lot, like, I think JS Contrive also has the same versioning problem, and if you import something from there, it should match something that works on the other people, so I don't know how we can fix that, but I think
If you can have a single entry point for users, that is the browser repo for them to install in their, like, as clients for them to install, maybe it'd make it easier for them.
**Jared Freeze (embrace)** 18:07 Yeah, I guess I have a question, too. So, like, I noticed that it jumped from, 0.57.2,
to zero dot… 200.
dot zero.
**Daniel Dyla (Dynatrace)** 18:17 Yep.
**Jared Freeze (embrace)** 18:18 So, what… what is the… what's the process for getting from 0 to 1?
**Daniel Dyla (Dynatrace)** 18:25 The process….
**Marc Pichler (Dynatrace)** 18:27 Please… oh, sorry.
Go ahead.
**Daniel Dyla (Dynatrace)** 18:30 Go ahead, Mark.
**Marc Pichler (Dynatrace)** 18:32 Okay, then I will… I will start. So, there's…
multiple things that you need to get from experimental to stable. The first one is all the dependencies should, of course, be stable. The semantic conventions should be, stable as well.
These are, like, the main blockers for most of the instrumentations today. So the instrumentation-based package right now is experimental still, and that's because we're dealing with a lot of,
changing environments that, like, kind of make it difficult to lock one consistent interface down. And the semantic conventions, obviously, is a large one, because once semantic conventions change, and you're already stable, then you're kind of in the word of hurt.
That's, something that everybody kind of ran into. And for the SDK packages, that is mostly, …
have to figure out that the interface matches what the spec says, and then you basically get a review from the TC, and then get that to Stable. So that's what we're working on for the logs SDK right now.
And the API, of course. So there's, these, these different things, that need to be done, and I guess one of the issues that we have in the JS repo, was that, like, there's no real focus on
getting anything to stable. It's always, let's start something new, and …
do something interesting and start from scratch. And then when it actually comes to doing the hard things, like making, breaking changes that are necessary to align with spec or do other things, then that is the less interesting parts. So these get usually left behind.
…
Yeah, so that's kind of the reason why these aren't marked as stable yet. And then there's also another thing that you have to consider when marking things as stable is that the spec has stability guarantees and requires you to
Maintain things that you have marked as stable for at least, one year.
… So if you bump from 1.0 to 2.0,
you will have to maintain 1.x for…
a year, still. So if you want to rev the major version quickly, let's say you do
major versions in one year, you will end up with having to support two major versions for an extended period of time, which will slow down development even more.
So… there's…
These different things that need to be considered before marking something as stable, so you need to be kind of extra sure.
Then you're going to be able to take on that, work.
**Jared Freeze (embrace)** 21:40 Cool, thanks for explaining that.
**Daniel Dyla (Dynatrace)** 21:43 Specific to the jump from 0.57 to 0.200, that's because we actually released a version 2.0 of the SDK.
And because all of the SDK packages are…
sort of tightly coupled. We made the decision at that time to rev the,
to jump all of the experimental package versions as well, because they depend on the SDK packages, so it's to show that, like, this is for the 2.0 SDK, so anything that's 0.200 is for the 2.0 SDK. Anything that's before that was the 1.0 SDK.
**Joaquín Díaz** 22:28 Yeah, also, I'll just say that…
I don't know about the node APIs, but I know the browser is constantly changing, so I…
It's, like, if you're saying they…
the semantic version is always experimental, because stuff is changing. That is also going to have it here.
But I think, like, if we can establish some baseline on, like, something that is
Basically, available across all browsers.
to reach a stable semantic obsession for something that is browser-related, maybe the hubs, at least for us, I don't know.
But again, like, that's a pretty tough burden to follow, because…
everything is constantly changing. You have multiple browsers with multiple APIs that are different, or, like, something's new on one browser, and it's not available on another browser, so you have to have that in mind.
Yeah, those, like, the most…
higher problem to solve right now. It will be versioning, if we have a new repo.
**Daniel Dyla (Dynatrace)** 23:27 Yep.
Let's call time on this. I think we, you know, need to get our thoughts in order here. The short answer for me is that no, I don't have… I'm not strongly opposed to this.
I just think that there will be some caveats. We only have 5 minutes left, and I do want to hear, from Thomas about this last topic that he added. Does anybody have…
Objection to moving on.
Sorry, Thomas, you only have 5 minutes.
**Thomas Hunter II (Datadog)** 24:01 No worries. Thanks for having me. Yeah, I'm, Thomas at Datadog. So we've got, …
bunch of customers who are using WebSockets, and of course, we'll have them use it for Server 2 browser stuff, but we actually have a fair amount of customers that use it for Server 2 server communication.
And so we've, … we've got, implementation in Java.
PHP, Python, and one coming in Node. It's sort of, like, like, experimental flag stuff that has to be enabled, but, you know, we also have, like, an RFC for it.
And, …
Sort of the implementation we're… we're using is that these things are able to, like, generate traces, spans, we even have a sort of a spec for
Like, distributed tracing, trace ID, passing along, stuff like that.
And so I'd like to, propose this as a spec for…
OpenTelemetry, and I did join the, semantic conventions group, but,
Obviously, there's a bunch of overlap with this, and browsers, and so I thought it would be useful to sort of join this and see if anybody had looked into this before, prior art, you know, I guess I don't want to…
necessarily step on too many toes with the proposal, but I'm also curious if other folks have vested interest, if I should just go ahead and create, like, a…
RFCPR somewhere.
I don't know if anybody had any suggestions.
**Daniel Dyla (Dynatrace)** 25:41 I don't know of any prior art within the OpenTelemetry organization. I do know that there have been some attempts at WebSocket, instrumentation
You know, by third parties.
… I think the best place to start is likely semantic conventions.
… The typical process is to…
Make a project proposal in the community repo?
… I'm sure that folks from here
Would be interested in that. …
But, as you said, it's not a JavaScript-specific thing.
I am less…
familiar with the specifics of, WebSockets, but to my understanding, it's, somewhat similar to, like.
It shares a lot in common with messaging.
So that may be a decent starting place is to also go to. I know that there is a messaging semantic invention group right now.
….
**Thomas Hunter II (Datadog)** 26:53 Good point, yeah.
So… Full, duplex, bi-directional channel, much like messaging.
**Daniel Dyla (Dynatrace)** 27:02 Yeah, there's also an RPC group, so that might be worth joining.
Yeah, I mean, like anything else, there's a lot of overlap with other areas.
But yeah, the typical process for something like this would be to… create a project proposal.
That outlines…
What you're trying to achieve, and timelines, and that kind of thing, and who you have committed to working on it.
As well as getting
A sort of specification sponsor to help drive any specification work that needs to be done, including semantic invention work.
**Thomas Hunter II (Datadog)** 27:40 … specification sponsor?
**Daniel Dyla (Dynatrace)** 27:43 Yeah.
Sorry, that's what I am in this group. It's essentially somebody who is used to working in the specification or semantic conventions that knows the processes there that can help, if changes need to be made, help drive them, because it can be a somewhat daunting process, for first-time contributors.
**Thomas Hunter II (Datadog)** 28:06 Cool. … Do you have any recommendations on how I would find one?
**Daniel Dyla (Dynatrace)** 28:12 So, I would go to… …
I would go to the spec group, probably, or the semantic invention meeting. A lot of the specification sponsors, for, you know, obvious reasons, join those meetings.
And try to find people with, either… Interest, expertise, or both?
… There's also a list of specification sponsors in the community repo.
… And…
like, the other SIGs that they are sponsoring, and if you find relate… like, if somebody is already working on messaging, that might be a good, …
place to start. I can't commit my time
right now, but I might be able to… I might be able to help sponsor that group, I just have to look at my time and availability and that kind of thing.
**Thomas Hunter II (Datadog)** 29:12 Awesome.
Thanks for the information.
**Daniel Dyla (Dynatrace)** 29:15 Yep. You need two sponsors for a project. Just to be clear, you don't need, a project to get stuff done in the spec.
It's just…
that's how you get, you know, a weekly SIG meeting, possibly get your own repos, you get a team to mention, you know, if you need code ownership in
Submit to convention repos and stuff like that. …
That's what enables all of that.
**Thomas Hunter II (Datadog)** 29:44 Cool, thank you.
**Daniel Dyla (Dynatrace)** 29:56 I guess that's it, then. We're out of time.
Thomas, you can feel free to reach out to me on Slack, if you're interested in more info.
….
**Thomas Hunter II (Datadog)** 30:08 Will do.
**Daniel Dyla (Dynatrace)** 30:09 Other… other than that… I guess that's it for this week.
**Thomas Hunter II (Datadog)** 30:13 Thanks.
**Joaquín Díaz** 30:14 So….
**Daniel Dyla (Dynatrace)** 30:15 Somebody mentioned creating a doc for the, the pros and cons for the new repo. Did somebody take that, as a…
Any… anybody volunteer to actually do that?
**Jared Freeze (embrace)** 30:27 Yeah, Joaquin and I will work on that, and I'll post a link back. I guess I'll just throw it into Slack.
**Daniel Dyla (Dynatrace)** 30:34 Awesome.
**Joaquín Díaz** 30:37 Yeah, yeah, we'll have that, and then if you can continue reviewing the other document, that's also great, so we can, like, start breaking down the work.
**Daniel Dyla (Dynatrace)** 30:48 Sounds good.
**Jared Freeze (embrace)** 30:50 Cool, thanks a lot.
**Daniel Dyla (Dynatrace)** 30:51 Bye. Yep, thanks.
**David Luna Bistuer** 30:53 tonight.
