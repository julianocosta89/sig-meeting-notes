SIG: C/C++ SIG
Date: 2026-02-04
Duration: 14 minutes
Zoom Recording URL: https://zoom.us/rec/share/uH2izu2XNzb1_6InjWAKUULNryzgJnyLGkE_Qvt_pVMN6Dwk2ToS9aaN93NU54r9.nGK8V3hD-nG_P747
============================================================

## Zoom Recording Transcript

**malff** 02:43 Hi, Tom.
**Tom Tan** 02:47 Hello, Mark. Good afternoon.
**malff** 02:50 Hi.
Sorry I didn't make it to the last meeting, had some conflicting, appointments.
**Tom Tan** 03:08 Yeah.
Okay.
**malff** 03:12 So, do you know if, Lalit is joining?
**Tom Tan** 03:16 I think he will… he probably will not join.
And maybe for the following a few weeks.
**malff** 03:22 Okay.
Okay, I don't have a lot of things to discuss. I saw that you created an issue to have an extra release, and I agree it's time we do one.
Because the previous one was in, glee cluster.
**Tom Tan** 03:47 explore that.
Before the vacation, right? Or…
**malff** 03:50 Yes, yes.
**Tom Tan** 03:52 Yeah.
**malff** 03:53 So, I don't remember the exact date, but it was… it's getting old, so we need to do something.
**Tom Tan** 03:59 Yeah, I think so. I think we have quite a few fixes. I have a few, like, for ETW Exporter, a few fixes.
I think we don't want them to be included in our release.
**malff** 04:10 Yeah.
Yeah, end of November, yeah.
**Tom Tan** 04:14 Yeah.
**malff** 04:19 There are a lot of commits, but now these days, a lot of them are just, very dependable fixing labels, so it has some noise.
But nonetheless, we still have a lot of things to… that we need to ship, so, yeah.
Beautiful.
You mentioned the PR from Owent, about the build with Windows Protobuf as a library. So, I looked at the code, I could not do a full review of that, because it's way… too complicated for me, but since you approved it, and since the CI is passing, I just merged it earlier this, this morning. So it will be part of the release.
**Tom Tan** 05:03 Yeah, yeah, that's… that is, that blocks something narrow, like, for Windows, you can't… use OpenTelemetry C++, as a shared library from… from two… two… two modules in the same application, or in the same process. Yeah. Because then, yeah, that will be helpful, that way.
**malff** 05:23 Okay.
And, there is another thing which… why it is?
There is a thing I just, discovered today, which is related to CMake.
Somehow, I was trying to… to do a demo of OpenTelemetry, but using, not using the Git branch directly, but working on an installed package, and somehow all the semantic convention headers, we just forgot to install them.
Have you seen, Duga lately? Because, I don't… I haven't.
**Tom Tan** 06:05 Actually, in the last meeting, maybe he didn't show, or didn't attend, maybe last few, I didn't see. I haven't seen him.
**malff** 06:14 Okay.
Because otherwise, we'll have to take a look at how to do the CMake install for that.
So it's not really urgent, but we are just missing instantly the installation of a bunch of other files.
**Tom Tan** 06:29 I think. Probably tagged him, or already tagged him in the issue, to see if he could reply.
**malff** 06:37 Yeah, I can… We can try.
**Ehsan** 06:49 Hi, everyone.
**malff** 06:52 Hi, son.
**Tom Tan** 06:54 Yes, Anne?
**malff** 07:17 Okay, so not… not really… notorious, anything is new on issues. One thing, which I mentioned in the… In the meeting notes.
In the spec, there is… the spec for propagation using environment variable is done, and there is an effort to implement that in every SDK.
So, there is a PR for that in, Hotel CPP already.
which is… This one?
And, so the reporter had a couple of questions for us. I took a look at the spec, I mean, at the PR, I can reply on that in some cases, but do you… You want to take a look as well?
The… The whole thing is to implement, propagators and, well, propagators we have, but it's to read and write from the text map, to set and read and write environment variables, when a process is forking something else.
So, Valger stood at some… some questions about how, if this is the right way to proceed and whatnot. I took a look at the PR overall, it's, It's, it's in a good path, just those questions that needs to be clarified.
Oh.
If you… if you have… if you don't have time, I can take a look as well, and start to reply.
**Tom Tan** 09:04 Okay, thanks.
**malff** 09:06 Okay.
**Ehsan** 09:07 Thanks.
**malff** 09:20 And… The other thing is still… still on the build area. There is this, PR that, Lalit just approved today, I think.
So I will merge that, before making the release, so it's actually part of the next release.
**Tom Tan** 09:42 Sounds good. Thanks.
**malff** 09:43 Okay.
Do you have any… anything you want to discuss otherwise?
**Tom Tan** 09:54 know from… Do we have a, like, do you… do you think we could, like, release a timeline for the release, or… As we… I think we don't have.
**malff** 10:04 to wait any significant PR, I think mostly…
**Tom Tan** 10:08 We're ready, right, for the new release.
**malff** 10:10 I think, yeah, we are ready. I will just merge the one which is already approved, but that would be done right away.
And I'm not aware of anything blocking that needs to be done.
So, I can prepare the release this week, then.
**Tom Tan** 10:26 Okay, thanks.
Yeah.
That's, all from my side.
**malff** 10:32 Okay.
Just a question for you and Nissan in general.
So there is this list of things that, people can pick up to, work on OpenTelemetry.
It has been working okay so far, because some people picked a lot of items from that list.
But I haven't seen any, any recent changes there, so… I'm wondering if we should, maybe I'll advertise it more, or maybe add more items to the list.
To ask, contribution on specific areas, for example, things like that.
Trust as a way to have, If someone wants to contribute as a way to have some, a list of things that are, ready to do, I guess.
**Tom Tan** 11:36 Seems there are still many open items in the contributor… contribution page, alright?
**malff** 11:44 Well, I forgot to change this one.
We have some open items, but I think we don't have enough, so that, people, when they see that list, they will maybe think, okay, well, not interested in this, I don't know how to do that.
And then they don't look beyond that.
**Tom Tan** 12:07 I see.
**malff** 12:08 If we had more items, Maybe there is a chance that, people will, We'll have an easier time to find something to do.
I don't know.
**Ehsan** 12:32 Could we add tags, like… Do we already have this help one?
**malff** 12:36 Well, yeah, all these are tags, I mean, those are the good first-issue NL prompted tags.
Every… Every item there.
Should have those tags.
**Ehsan** 12:51 Yeah, yeah, I mean, one link for the tags, so they could also… Check them in one place.
**malff** 12:59 Okay.
Could be, yeah.
**Ehsan** 13:03 So, like, we have this list, if it's not enough, you could click here, you get more.
Which is less focused, maybe.
**malff** 13:14 Yeah, I can… I can look at that.
**Ehsan** 13:17 Thanks.
**malff** 13:23 Okay, so, that was just a question on these lists, otherwise I don't have any specific items.
**Ehsan** 13:35 Alright, me neither. Tom left already.
**malff** 13:38 Yeah, got disconnected, maybe.
Okay.
Well, good to see you again. In that case, I think we can close the call, because I have another meeting coming soon as well.
**Ehsan** 13:49 Yeah, thank you. Good to see you.
**malff** 13:51 Thanks, Azan. Nice meeting. Bye.
**Ehsan** 13:54 Bye.
