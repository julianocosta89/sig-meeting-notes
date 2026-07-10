SIG: Browser SIG
Date: 2026-07-09
Duration: 33 minutes
============================================================

## Zoom Recording Transcript

**Jared Freeze** 00:44 Hey, Jared.
**Jared Lewis** 00:47 Hey, Jared.
Are you in Honolulu?
**Jared Freeze** 00:51 Not at the moment. I'm in,
**Jared Lewis** 00:54 Okay, no problem.
**Jared Freeze** 00:55 New Orleans, Louisiana.
**Jared Lewis** 00:57 Oh, I lived there for a little bit.
Basic.
**Jared Freeze** 01:01 Thanks.
**Maxime Quentin** 01:19 Hello.
**Trent Mick** 01:23 Sure, they're gonna be showing us.
**Jared Freeze** 01:26 My what?
**Trent Mick** 01:26 You showing off with the sunglasses and everything, or…
**Jared Freeze** 01:30 Are you a Celsius person?
**Trent Mick** 01:32 I am a Celsius person, yes.
**Jared Freeze** 01:34 It's 32, and lightning took out my internet, so I'm outside.
**Trent Mick** 01:40 Cool.
**Jared Freeze** 01:41 Okay.
**Ted Young** 02:06 I was rocking the sunglasses, but it was because I had my eyes dilated, so I had to be the cool guy for a bunch of meetings.
**Jared Freeze** 02:15 Bye.
Welcome back.
**Ted Young** 02:18 Thank you.
**Martin Kuba** 02:39 Anything we want on the agenda put in. If you want to talk about about anything, put it on the agenda.
let's just wait one more minute, I guess.
**Jared Freeze** 03:08 Yeah, it's an Argentina holiday. I forgot Aquino won't I don't think he had anything to add.
Nevertheless.
**Martin Kuba** 03:25 Okay, let's get started, I guess. I have one topic.
We have been working on the SDK package which has been merged. It's not. It's not published yet. And I wanted to see if there's any objections of going ahead and publishing it. If not, I have.
Open the PR to edit the… Release, please, process, and… Yep.
**Jared Freeze** 04:01 Do we have anyone willing to… Install it somewhere. I don't know.
Like, does anyone have a… Good candidate to get started.
I can definitely try to put it on… I mean, I have a personal homepage that nobody looks at. I will visit it here and there.
And then… Sign up for… something?
So the data goes somewhere?
**Maxime Quentin** 04:42 I could, like, update maybe the sandbox to use the official… Release, and then… On the side, we have, like, tests that are generating the data.
Could be a first step.
**Jared Freeze** 05:00 Do you want to have it?
Try to hit localhost.
With cores, or something?
And then we'll just spin up… Like, a local collector?
**Maxime Quentin** 05:13 Yeah, I mean, we could improve the sandbox to have some kind of a better, Collect our implementation and maybe see, like, live what's going on.
Yeah.
I have no clue how we should proceed on that, but if you want to discuss about it, I could take the point.
**Jared Freeze** 05:36 Yeah, I mean, it would have to be hosted. I'm not sure how that might work within the official org.
But, yeah.
**Maxime Quentin** 05:45 Yeah, I think with Martin, we tried to find a way to do that.
On my side, I could not find an easy solution.
How to… how is the data we send? But, At least a visual… better visual feedback on what is happening, What we are instrumenting, and stuff like that.
Inside the sandbox could be a first step.
To help people like ramping up on the SDK implementation and how to start to strike their SDK.
**Jared Freeze** 06:23 Yeah, that sounds good to me. Yeah, just modify the sandbox.
I'll see… There may be… A vendor, one of our partner vendors, that could put up a free account if we do want something hosted that's, like, a little beyond what we're talking about here. I will… Make a note of that.
**Martin Kuba** 06:49 Yeah, also, aside from hosted, we have, we have that demo… branch which has a collector. So for anyone, I think we should.
for anyone who wanted wanting to test it locally. That's available.
And we should update it with the with the SDK.
Also, once we release, I want to make a bunch of updates to documentation, too.
I'm… And examples.
**Trent Mick** 07:18 Like the top-level README and things like that? I was going to ask about that, too. OK, that Do you know if anyone in this group will have the bandwidth to look at or maybe it's premature? I guess I'm asking. Updating the hotel demo.
To be moving to this and away from the other.
Like, SK Trace Web, and… Those packages are not…
**Jared Freeze** 07:42 Yeah, I actually have somebody, at our company that's not in this group, that's part of the demo group. I can pitch it to him, because I think he picks up tasks there.
**Trent Mick** 07:53 Okay. Okay. Do you guys feel like it's, you guys would be happy that if the demo moved over to doing that now instead of?
So long in the 2 older packages, or.
**Jared Freeze** 08:06 I mean, things are changing really fast, like, as far as our… You know, surface, so.
I mean, yes, but I think we'd have to have somebody stay on top of it.
Just because the API is going to go out of date.
Until we reach 1.
That would be one.
**Trent Mick** 08:27 Okay.
Okay.
**Jared Freeze** 08:28 I mean, as long as we manage it, I suppose.
**Trent Mick** 08:32 Okay, maybe a slightly more targeted question. So, background for some others. I work mostly in the OTelJS repo, and mostly on the node side of things, and one of the… refactorings that we've done recently is we've made an SDK Trace package, where there used to be 3 separate packages. There was SDK Trace Base, SDK Trace Node, and SDK Trace We We've released SDK trace, which mostly the reasoning for the change was tracing was the first signal. And when the SDK packages were being built, that's the one that developed a lot of kind of design warts.
And since then, SDK metrics and SDK logs, logs being more similar to tracing on a signal.
cleaned up a little bit how we wanted to handle things. One in particular was configuration handling, so… Sdk Trace Node had embedded, like.
reading environment variables and stuff like that, which, when declarative config came along, wasn't really the right way to to construct that kind of stuff. So Sdk trace package is a bit… simpler in that it removes some of those pieces. And so I'm most of the way of… moving all the packages in the OTel JS contrib, repo over to use SDK trace instead of the dash node and dash base versions. But dash web, I haven't really moved over yet 'cause there's not, or moved anything over away from SDK trace web because.
The two pieces in there, one is the web… Tracer provider, Mostly because that sets up the context manager, defaults it to the stack context manager that lives in that package. And then also there are a few utilities in SDK trace web package that were being used by some instrumentations. I think mostly there's a clear path.
there, and that those utilities are moving over to the individual instrumentations as they move over, so that one's a little bit clearer.
My understanding is that the get default context manager in the new browser SDK package is the same as the stack context manager.
From SDK Trace Web, so… My hope was to be able to moving things away from SDK Trust Web is to be able to use that stack, or that context manager from there, and then maybe that's, like, that's the blessed future one. I don't know if I… if I run into a cross-repo dependency issue that makes it difficult to move some of the cases over, but we'll see.
Anyway.
So that's not so much a question, it's just raising awareness.
**Martin Kuba** 11:13 So that that's those other trace packages are being deprecated completely. So I'm not. I'm not actually sure like if we have them referenced in.
We should check in. Yeah.
**Trent Mick** 11:28 Yeah, for example, like the README demo at the top of the web.
Or the browser repo.
is still using SDK Trace Web, but that's just 'cause you copied over the way it was being done before and you didn't have the SDK package. So as you said, you'll update those docs. Yeah. Yeah. If I run attending blocks, I'll ask on your Slack channel and come here to meetings and things.
**Martin Kuba** 11:51 Okay.
Thanks. Thanks, Terence.
**Trent Mick** 11:55 Yep, sure.
**Martin Kuba** 11:59 All right, so it sounds like there's no objections to releasing that.
SDK package. So yeah, I have a link to the PR to… to enable the automatic release process, so if you… take a look and Review, that'd be great.
**Jared Freeze** 12:18 My only feedback there is, do we want to start at 0.1.0?
**Martin Kuba** 12:25 Umm… Yeah, I think what we did with the instrumentation. We we did the initial Release with.
0.1.
and then then release release. Please did like picked it up at 0 dot 2.
Okay.
**Jared Freeze** 12:48 Yeah, I guess my question was more, does release, is release please aware.
Of what versions need to be bumped for the SDK if it's changing alongside.
Like, is it… is it aware that it… Good.
There's things outside the package that could affect its version number.
Right? Like, if it pulls in utilities or something.
I guess I don't know enough about it. I can, I can read that, I suppose, but If it's gonna bump… in the same amounts as the instrumentation, I would almost want it to match And forgive me if this is settled, I just don't remember the conversation.
**Martin Kuba** 13:32 Yeah, there's no cross dependencies right now between those two.
And.
I think they can be. They can have independent versions, but Because I think what we decided was, that yeah, for for like the SDK, like this, like semantic versioning like would be like the indicator of stability.
as opposed to like with the instrumentations, because we have different instrumentations that have different stability.
There would be, like, the path, the export path was, like, the indicator there.
Right, so…
**Jared Freeze** 14:06 Yeah, that makes sense. Okay.
Cool.
Yeah, then I think… Yeah, I think we can get that merged unless anyone else has feedback.
**Martin Kuba** 14:24 Alright, the next topic is Ted.
**Ted Young** 14:29 Yeah, I think, we're, we're moving along at a pretty good clip, and so are some of the other clients, and one thing I think that would benefit all the clients right now, is another round of… kind of socializing more, more with each other, and then more with, like, the SemConf SIG and, like, the general spec, like, other SDK maintainers SIG.
I think just… it would be nice to get, I think, a little more structure going across, like, with cross-client concerns. One place, we're looking at that is, Federated Semconf.
Right? So semantic conventions have added tooling so that we could create a separate repo to put our semantic conventions in.
Seems like it would be useful not to have a repo per client, because there's also cross… You know, semantic conventions we're using that are generic semantic conventions, semantic conventions we want to share with other clients, and then our own specific stuff.
But having our own repo… of like shared client conventions might help.
Clarify, like, what the actual structure is.
But I think if we do that, we need to make sure that we're… going to the Semantic Convention meetings more, presenting there more.
I think there's a presentation on network timing events, and I actually have some follow-up questions about that, but I think it was an example, maybe, if there was some confusion between, for example, how HTTP clients are normally modeled as spans, but because what we're doing is we're trying to model data that's being handed to us from the browser, right? So, like, a browser event. It kind of, like, looked weird.
to them.
That's actually, I think, an issue we still need to solve. I added that to the agenda just as a link to the comment for people to have a look at.
But… It just feels like it's good timing to maybe be sharing what we're doing and also kind of like asking questions. It would be helpful to get someone with client side expertise onto the TC. So the TC is looking for candidates for people.
Potentially to fill that role.
And, We have, like, a client SIG that kind of went dormant when we separated the SIG out, but maybe rebooting that as well.
And last but not least, there's this, SpecSig, that's just more like general maintainers from different SDKs, meeting and discussing various issues.
It would be good to, I think, present there soon. It sounds like we're kind of, like, in a… getting to a point where we're… we're ready to present something, but it would also be good to socialize the fact that, you know, we're going a different direction in terms of our SDK design to the browser constraints.
things like that.
So, bit of a ramble for me, but the general thing is, like, trying to find ways to be checking in more with other SIGs, because I think that's… seems to be, like, our primary way of avoiding issues where we get a lot of work, and then we kind of, like, surprise other people, or we get told, you know, hey, our designs aren't lining up with what other people are doing. It's also a good way to get help.
And I think especially with the other clients all developing things in parallel, making sure that we're kind of keeping track of things that we want to have shared across them.
there's a new, SIG that would like to form around Flutter, and since Flutter is, like, a cross-platform client, I think that's really gonna, like, push the need, especially around semantic conventions, to figure out, like.
you know, what's shared versus what's specific, and, like, what should Flutter be doing, if they're… they're cross-client? Like, should they be having, like, Flutter-specific conventions? Like, how should they… how should they bridge that gap?
So, again, just a bit of a ramble, but I think mostly, just… camping out in some more channels and attending some of the other SIG meetings. If more people from this group could start doing that, I think that would be like a good starting point, just to just to socialize a bit more.
Curious what you all think about that.
**Jared Freeze** 19:28 Yeah, I saw the message come in, So I actually work directly with Hanson, who is hosting that demo repo, or whatever you want to call it. It's Those semantic conventions are taken directly from our Android product, and so those are sort of settled. I love the idea. I thought the name was a little long. End user clients seems redundant, but… Yeah, love the idea. I love that it's Weaver. And I would absolutely be willing to go to wherever semantic conventions for clients are going.
So, yeah, whatever meeting that is, or channel, or whatever I'll pop into, because I do think… mobile… yeah, mobile is not consistent, and I would love to be included at the beginning. Like, we should be included at the beginning, of all this, so… especially with Kotlin, Flutter, whatever else is coming, you know. Mobile moves quick, too, Not just web, so…
**Ted Young** 20:28 Yes.
Yeah, and we have, like, iOS, for example. The iOS crew has definitely been kind of, like, floating in space off on their own for, like, a long time, so I'm also going to them, being like, come hang out, come hang out with the other clients.
So.
it feels like good timing to kind of figure all of that out. And if we feel like we need more structure as well.
We're trying to figure out how to structure these things a bit better. And what I mean by that is like, we have some SIGs. We might, you know, be able to get some more representation on the TC. But like, do we need some kind of structure around some people, you know, having it?
Having some time carved out to be, like, looking across the different clients.
and trying to like actively coordinate across the different clients like, is that helpful? Or is it enough just to have maintainers from different clients kind of colluding and working together. I don't. I don't have a a strong opinion on that one, but it's worth. It's worth considering.
Is it just? Can we all just kind of work in a flat system? Or does someone need to be like actively doing research and coordinating in order to make sure that like… like, things are shaping up into, like, a coherent hotel for clients kind of system.
Also, does anyone have, like, time to do that? It's, like, the other concern that I have.
**Martin Kuba** 22:03 So, Ted, I have one question. Like, in the past, like, I think we had, a TC member, like, assigned to each SIG.
Is that still… still a thing?
**Ted Young** 22:16 There… there is a… sponsors for, like, projects when they're booting up. Implementation SIGs tend not to have sponsors.
And the other issue we've kind of had is, like, the TC is all frickin' server-side jockeys.
So they don't necessarily, they bring it, they have a lot of open telemetry design expertise, but this isn't really a domain they have.
there's anyone on the Tc. That like has an interest in, or or like deep knowledge in, and And that's like.
So I don't totally know how how helpful it is to have them coming here. I think we can solve some of those problems by just being more proactive.
When we're thinking about design decisions and just making sure that we're surfacing them Umm.
In the spec meeting and surfacing them And in the maintainer channel, So I'm adding some links to, like… there's OTEL client-side telemetry, there's also OTEL maintainers, which, to be clear, like, you know, approvers and other people can hang out in, but… These are channels where we can, like, socialize what we're thinking about with the other SDK maintainers, because there's feedback from the TC, but there's, like, also just, like, lots of other maintainers who… who work on OpenTelemetry.
and trying to figure out going forwards to make the TCB less of a bottleneck.
I think one of the solutions is the maintainers as a group just working more with each other on designs.
Oh.
So those are my thoughts. I would say a concrete next step is there's two channels, OTel client-side telemetry and OTel maintainers camping out there.
maybe presenting at the spec meeting.
And… getting federated Semconf put together, but also as part of that.
Working with the maintainers of the main SimCom repo to, like, make sure we don't just go off in a corner and start defining things. Like, I think the resource timing, the way that conversation went, seems like a good example of, like, we should just be talking to them more So there's more of a shared understanding of what we're trying to accomplish and how that might be different from from what a lot of the other semantic conventions are.
Because I think there's some cases where we're maybe doing our own thing, because we just don't know any better, because we're off doing our own thing. And there's other cases where the… the clients, especially the browser, are, like, a different environment, so we're modeling them differently. Like, in particular, we're using a lot of events, and part of that's driven by the fact that we're getting information about what's going on asynchronously from the system.
And that makes it a lot harder to, like, use spans and other things.
In certain cases, because we're more like, we're trying to model just what the browser is giving us and report that back.
Rather than… like redesign how the browser should be reporting information to us, you know.
and just making sure that that stuff is getting kind of socialized both ways would probably be useful.
**Jared Freeze** 25:57 So back to your very first statement, I'll talk to Hanson. I think Hanson has an appetite for sort of leading, like, sort of, you know.
You know, where these things like come together. So maybe for semantic conventions, at least for the federated stuff, he'd be willing to look at the different groups. So across all mobile and web and whatever else comes along.
Yeah, so…
**Ted Young** 26:21 Cool, yeah.
**Jared Freeze** 26:22 No.
**Ted Young** 26:23 and yeah, I'm hoping to get Hansen or someone to to also kind of report back to.
the spec SIG. One thing people, when I say report back, something we've been doing in that meeting, people haven't been going, and I'd love to maybe start recording these or putting them out, is just having different projects do kind of presentations on, like, what they've been up to and what they're working on, and people have been finding those, like, really informative.
Just the projects big enough now, like OpenTelemetry, there's so many things going on in parallel that it's very hard to keep track of what everyone is working on. And just having different projects come present what they've been up to has been really enlightening.
So, certainly a presentation of the browser working, and it seems like we're getting close to a place where we'd want to do that would be helpful. But I think the other presentation is sort of, like, client-side telemetry in general, and, like, what all the different SIGs are doing, and, like, kind of how we see it is, like, different from server-side, like, where are the places we see things differently?
what are the… the sticking points that we've been having with the RISC community around, like, session management's been, like, a big one.
So I might poke Hansen to try to put that together as well, since we're he's not here, and we're assigning work to him.
Okay.
So running out of time. And again, not anything too specific except to have a look at the federated semantic conventions and just make sure that you're in some of these cross-SIG channels so that we can have some more conversations there about how to figure out.
Like, what amount of structure feels like it's actually helpful versus just annoying?
Q. That's all I got.
**Martin Kuba** 28:30 Okay, well, I think we're at time, so.
If there's nothing else, then.
I can call it.
**Jared Freeze** 28:38 Cool, thanks all.
**Ted Young** 28:41 Yes.
**Trent Mick** 28:41 Yeah, sure.
