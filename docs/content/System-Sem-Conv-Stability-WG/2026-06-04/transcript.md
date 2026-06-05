SIG: System Sem Conv Stability WG
Date: 2026-06-04
Duration: 29 minutes
============================================================

## Zoom Recording Transcript

**Donal O'Sullivan** 00:20 Hey, Roger.
**Roger Coll** 00:23 I don't know.
Oh, yeah.
**Donal O'Sullivan** 00:26 What a roof.
Yourself.
**Roger Coll** 00:31 Good, as well. Let's see if we… We can share this host metric thing.
Not a precision, let's see if there's something on the… agenda, not… Didn't remember to add it.
**Donal O'Sullivan** 00:48 Yeah, I'm not familiar. I need to actually read it. Essentially, the issue seems to be that Instead of dividing two integers.
The integers are reconverted to floats, and then that… the division happens on the floats, which is then given in a result which can vary.
**Roger Coll** 01:10 Yeah.
Yeah, exactly, so the… The issues that gobs utils… Converts the, let's say, the row integrals to floats.
And then, that's the division.
So, on this conversion, you are already losing some precision if you have a large, Numbers.
And… And instead, let's say… and it's, what Salvatar said, that if the, depending on the absolute counter, right, if it's very big.
You might have, different… Yeah, different, different values, and… Yeah.
While his solution, it's the other way around. So you work first with integrals, and late, at the last step, you convert to, load numbers.
**Donal O'Sullivan** 02:08 Yeah, that seems to be the solution, yeah. If you do your integer division first, and then you… the final result is converted to a float.
**Roger Coll** 02:16 Yeah, exactly, that's.
**Donal O'Sullivan** 02:18 Yeah.
**Roger Coll** 02:19 That's why his reasoning, that it's a correctness thing, not the… Not a compression, as maybe we were…
**Donal O'Sullivan** 02:28 Yeah. Consider it.
**Roger Coll** 02:30 mute.
**Donal O'Sullivan** 02:31 Yeah, that definitely seems like it's probably a… like, that's actually a bug in GoPS Util, because it's going to give you, If that division is happening there, I think that sounds like it's incorrect.
**Roger Coll** 02:47 Yeah, I guess, I don't know if it's, like, you know, like, a decision that they took, because it's… It's API, it's agnostic to the OS.
So, maybe some other systems.
Gave it directly as art decimal numbers from the source, and… They just consider it that way, But yeah, well, let's… let's wait, maybe a couple of minutes and shed it out there.
**Dmitrii Anoshin** 03:26 That hooks.
**Roger Coll** 03:29 Right.
**Braydon Kains (Google)** 03:36 Hi, everyone.
**Donal O'Sullivan** 03:40 Blue.
**Braydon Kains (Google)** 03:53 I'm cat-sitting, I'm not used to having Cats rattling about behind me in the basement, wondering what they're getting into.
**Donal O'Sullivan** 04:03 Cats… cats can be funny, they'll jump up behind you when you're not… when you don't… when you least suspect it.
With the interest of time, I can start quickly, it's just two small things. Just the mDataGen PR is up, I think Christos has reviewed it, I think he seems to be happy with it. He said he was going to try and get to it again today, so… I guess, Dimitri, Braden, if you guys want to have a look at it, if you have the chance at some stage.
**Dmitrii Anoshin** 04:41 Yeah, I'll take a look. Thank you.
**Donal O'Sullivan** 04:43 Yeah, no problem, thanks.
And then, just quickly, the other issue was… I actually created a PR and semantic conventions to move process to release candidate.
Oh, Braden, you approved it, sweet. Okay, cool.
Thank you. Yeah, just, just, just bring it here, just for a heads up.
Thanks, Braden, I appreciate that.
**Braydon Kains (Google)** 05:07 problem.
**Donal O'Sullivan** 05:09 That's all I got.
**Roger Coll** 05:14 Okay. Hmm.
from my side, I just bring it again, the, topic that we discussed last, We… last week, about the… about the CPU values in… in the host metric receiver, about getting it directly from slash clock, or just… getting it from the GOPS utils, and I think, yeah, Dmitry, you had a chance to take a look, but yesterday. I'm not sure if you… if you saw the reply from, from Salvatore, and I also… we discussed it internally, and I think during last week, the point was more on the storage improvement, but actually, internally.
The point that they shared, it's… it's more on the correctness on the… of the values, not on the… On the storage, let's say, benefits, so it's, they see it as a… as a win-win, because, Because the actual, yeah, let's say the inaccuracy that we have at the moment.
And as far as I understand, the issue, or the root issue here, is the… well, there's two main cases.
And the first one, that it's the PR that, we shared is that, Basically, Bob's utils gets the raw integral values from the CPU.
usage.
And converts them into floats, let's say both of them.
And then that's the subtractions, but already as floats.
So, on this conversion, we might, for large numbers, we might be losing already some precision, and… We carry over, This inaccuracy, while his solution is the other way around, just… Get the integral values, work, do the subtractions for the utilization and the deltas with integrals, and the last step Convert those to the floating numbers.
And I think he added a case, maybe I can share my screen, but, yeah, let's say yak.
A case where, let's say the delta, it's the same, But, because the… Counter keeps increasing, and the absolute, let's say, counter, it's different.
And that counter is converted to a float from the beginning.
Let's say that the result is different, even if the delta is the same.
And that's why they… Or we see it as a… More as a correctness scene.
Mmm… So, yeah, it's…
**Braydon Kains (Google)** 08:28 Sorry, I'm reading.
**Roger Coll** 08:33 Yeah, no problem.
I believe.
**Donal O'Sullivan** 08:50 It's actually called a catastrophic cancellation.
Don't bring anyone in.
**Roger Coll** 08:58 Christmas.
**Donal O'Sullivan** 09:07 Yeah.
**Roger Coll** 09:13 Yeah, exactly.
So yeah, it's more… So, so if…
**Braydon Kains (Google)** 09:34 If the most important thing for getting this right is… Mainly that we can… that we can… read the ticks as an integer from proc. That's the main thing, right?
**Roger Coll** 09:50 Yeah.
**Braydon Kains (Google)** 09:51 I know… so, GoPS Util does that conversion because of the, OS API like, OS ignorant API, like, they're trying to be cross-platform.
But they do have, like, Extension structs?
that… exist.
Per platform to provide information that only is important to that platform.
If all we need is the ticks, and then we can work with everything else. If we can get that into Go PSUtil, then we can avoid the thing that I… most to dislike, which is that for certain things, we would need to read and parse proc ourselves versus go psutil doing it.
And in this case, we'd need to… we'd be reading proc a second time, I guess, because we already need to read that file for something else, right? So, if there was any way we could maybe just get the tick integer into one of the, like, extension structs that we get back.
I don't know if that's a possibility, but if it was, we might be able to avoid implementing our own proc parsing for that scenario.
**Roger Coll** 11:06 Okay, I don't know about this extension thing in computers. Yeah, it's, it's…
**Braydon Kains (Google)** 11:13 mostly, used in… it's used most often in the Windows implementations of stuff.
**Roger Coll** 11:19 Hmm.
**Braydon Kains (Google)** 11:19 I think it's a reproducible pattern, though, if we need it just for Linux to get the direct tick values.
**Donal O'Sullivan** 11:29 So, like, it's just a field and a struct that you can pull a value from that's returned from calling a goPS util function or something like that.
**Braydon Kains (Google)** 11:37 Yeah, it's… it's… it ends up being, like.
I don't remember… I'm trying to… I'm trying to think of exactly how this… how this worked, but there was a way to… Like, the struct only ends up existing within that platform implementation, so if you try to use it without the proper GoBuild, you know.
**Donal O'Sullivan** 12:00 Yeah, yeah, yeah.
**Braydon Kains (Google)** 12:01 guards, it would fail. But then it makes it so that you can return platform-specific information.
**Donal O'Sullivan** 12:08 Okay, gotcha, yeah.
**Braydon Kains (Google)** 12:11 I'll see if I can find an example. If I can find an example… I will post it on… is this the issue or the PR that we've been talking on? This looks like the PR.
Yeah. I'll reply to the comment on the PR, then. Let's see if we can do that, because… I… I think I get it from reading, it's… it's… the math is not, fully clear to me yet, but I understand that The package doing a conversion means the original values are obscured, and thus we can't reproducibly Make the same value appear.
so I get that.
So if… If us exposing ticks makes it possible, and we can just do the math ourselves on the ticks, if it could be produced by… like OPS utility best, but I will check again after the meeting if I'm remembering correctly that, like, this is something that we could do.
And I'll, I'll reply.
to the… to the comment. And as for whether we should revisit, I think… Dimitri's comment, asked if we should revisit.
The original, like, precision… Library that was introduced.
I had kind… I had less of a problem with that, because it was mostly… what are you doing, crazy cat? Sorry.
It… it was… just, like, a math package. Like, it wasn't doing any special platform-specific behavior or, like, redoing work that GoPSTIL did, so I didn't think I had much of a problem with that, but… I'm open to revisiting it if we want to.
**Dmitrii Anoshin** 14:02 Yeah, from my perspective, we just… same comment. If it's not applicable to the latest, CPU-related VR, but it still seems to be applicable to the memory, where we just… Try to calibrate.
decimal precision of the Mandisa, which doesn't seem like… doesn't seem like a good idea to me.
Because it doesn't make the value… more… Correct.
It's rather just…
**Braydon Kains (Google)** 14:38 Yeah, this is a.
**Dmitrii Anoshin** 14:39 For example.
**Braydon Kains (Google)** 14:40 Yeah, when I was interpreting this PR, I was interpreting it as some kind of, Storage optimization rather than a correctness thing.
So I'm… I might come to a different conclusion if I look at it from that perspective instead.
**Roger Coll** 15:04 I remember correctly. Yeah, right.
**Braydon Kains (Google)** 15:06 Yeah, the first line of this, PR says it hurts downstream compression, so that's why I was thinking of it that way.
**Roger Coll** 15:12 Hmm.
**Braydon Kains (Google)** 15:13 Is that not the case, then? Or is the… or it is in this case, and not in the CPU case?
**Dmitrii Anoshin** 15:26 Yeah, I guess the… the catastrophic, like, oop, I forgot how it's called. When we… when we… Subtract.
some, like, low, low values of the Mantisa, and then we get an inaccurate value. That kind of makes sense if we can avoid that, if we can make it separate. But this one seems to be just a representation improvement and doesn't improve the color correctness.
Of the value itself. So, feel free to take a look, I can take another look, Braden, but if we agree that… I guess we should, first of all, we should agree on the… Requirement, that we don't want to… make any representation improvement of the value, that would hurt accuracy. We should always strive for the best accuracy in this receiver.
Does… does that… Something… but does that make sense? Do we agree on that?
**Braydon Kains (Google)** 16:34 I think so.
**Dmitrii Anoshin** 16:35 Okay, cool. Then, taking that requirement, we can revisit the RNC.
**Braydon Kains (Google)** 16:42 The main thing I'd like to clarify is, because the other PR mentions a downstream compression improvement, I'd like to know what that is. I think that the reason that we… The other reason I was okay with this happening here Is that… I didn't see any way for… Like, a transform pipeline to improve this?
like, I didn't… I didn't see any, like, OTTL functions or anything that would do this math itself. And so… I thought it was fine to introduce a precision package that would allow us to adjust the… the overly long… like, way too precise values and ratio them down. That seemed fine to me at the time.
If it's about ac… if this is more about accuracy, though, then I'm… I'm confused what the first PR was for, so that would be good to clarify.
**Dmitrii Anoshin** 17:43 Yeah, and the OCL function, I… don't have any pushback on that. It makes sense to introduce that.
a geo function. It just doesn't seem to be something that should be in general package of cost metrics receiver.
**Braydon Kains (Google)** 18:02 Yeah, I could… I could get behind introducing this as a… as a, OTTL function instead, if it would make sense, and especially if it would help, like, that's the other thing, I'm like, is there… now I want to know what the downstream compression case was, and I probably should have asked when I was first reviewing this, but I didn't really… I just kind of… Accepted it and moved on.
**Roger Coll** 18:25 Yeah, it makes sense. I will revisit this PR as well, because I'm not sure if we can do it in the… Farther down in the pro… in the processor.
Because I think the main ideas that, of this package was that you have the… Available the integrals before doing the, the division to float and to converting it to float.
And you were able, basically, to trim, or just to remove.
Let's say the… The added noise that adds the, the division, that it's… Not needed, knowing the unit.
Like, if you're on seconds, milliseconds, or you're dealing with megabytes, bytes, or something like that.
**Braydon Kains (Google)** 19:16 Yeah, right, I forgot about the… the timescale part of it. That actually wouldn't be doable in a processor. I don't… well… The time… the timescale one, specifically, probably could be.
But anyways, I… yeah.
**Roger Coll** 19:33 Yeah, but… Then you can… you cannot… How do you provide the utilization after the process or the utilization values?
Hmm…
**Braydon Kains (Google)** 19:47 the…
**Roger Coll** 19:48 Because you're.
**Braydon Kains (Google)** 19:48 Utilization doesn't get timescaled, does it? I thought that was just the, The raw time counter that was getting scaled.
**Roger Coll** 19:59 No, it's also the utilization, I think.
**Braydon Kains (Google)** 20:02 Isn't the utilization a percentage?
What is it getting scaled on?
I think that's a… the utilization was the ratio.
**Roger Coll** 20:12 But it's divided over the time delta.
**Braydon Kains (Google)** 20:17 Oh, right, over the… yeah, okay, over the… Oh yeah, scale is a confusing name.
**Roger Coll** 20:25 Yeah, go on.
**Braydon Kains (Google)** 20:26 Yeah, that's… that's… I'm confusing, because, because the… To get the actual ratio, you need to know how much time has elapsed.
**Roger Coll** 20:36 Yeah, exactly. Look here, it is the precision data over the delta total.
**Braydon Kains (Google)** 20:41 Yeah.
**Roger Coll** 20:43 Oh, so the.
**Braydon Kains (Google)** 20:44 The utilization is still using the ratio interface, it's the… and then the tick times are using the scale interface.
**Roger Coll** 20:51 Hmm, yeah, yeah, I see.
Mmm… Okay, well… From my side, maybe I will add them, just that I will review this PR and add a comment.
With the clarifications that we need, either if it's possible, from the processor's perspective, and If it actually adds value and correctness into the outputted values, and just ensure that, we have a… Clear and all that.
**Dmitrii Anoshin** 21:27 Thank you, Roger.
**Roger Coll** 21:29 No, thanks to you.
**Braydon Kains (Google)** 21:38 This… this is more of, an FYI, but… I agreed to organize a network semantic convention group, which is… Basically, like this group, but for the network namespace.
the reason I agreed to do it is… partially because I know there's some people at work who want to make changes, and they're all pushing into our group, and then other people are also pushing into our group to make network changes, but that's kind of… Outside of our scope.
So I agreed to organize the network.
group. They're going to now be the… Owners of the network namespace.
And I'd probably, like, add them on NEPRs to the system.network namespace that we'll still nominally own, but… My hope is that the division is sort of, like, Our group owns.
anything… Like, like, information that you'd scrape from slash proc slash net, or information about, like, network interfaces themselves, like, our group would still at least be involved in those, whereas the network group would be focused on things like the… recently, someone came to us with a big, like, TCP and UDP network metrics and stuff, and… that's kind of out of our wheelhouse. You guys probably actually know more about this networking stuff than I do, but, like, it's outside of this group's scope.
So, like, that sort of thing will get sent over there. Anything related to, like, DNS, or, like, network peer information, or the kind of things, like, the golden signals that eBPF solutions will be scraping, that's the sort of thing that I want to go to that group instead. So, this is mostly an FYI, and also, if you know networking people who would be interested in joining, have them comment on the issue as well.
**Dmitrii Anoshin** 23:39 Sounds good. Thank you, Ray.
**Braydon Kains (Google)** 24:00 The only other thing maybe worth mentioning, which is not semantic convention specific, but more host metrics receiver, is… the AIX… the… which I guess is, like, IBM PowerPC?
Platform?
the scrapers for AIX support are getting added over time.
and the… the contributor there had some… Ideas of how to handle this, like, platform support stuff over time.
I think the big… the big one they called out was… they sometimes… they work with customers who try and use the same or similar configs on both Windows and Linux, and the way metric enablement works when you do that means that you're guaranteed to get errors on basically both platforms, because if you're trying to enable metrics that are Windows-specific, like Windows only, like, don't work on Linux, they'll just, like, continuously fail on the one that's on Linux.
So, I'm working on designing an MDATAGen feature for, For declaring hardware support as, like, an annotation in the metric.
So that… mdataGen will know if someone has given, like, an enabled, but you're running on… enabled for a Windows-only metric, but you're running on Linux, it won't enable it, and it might emit a warning, maybe.
I'm not sure about that yet. I think it should, but… Anyways, I think that's… that's underway, I just have a lot of… a lot of stuff going on right now, I haven't gotten to it yet.
**Dmitrii Anoshin** 25:45 I think we're showing warnings maybe if they explicitly enable it, but for.
**Braydon Kains (Google)** 25:50 Yeah, that's what I was thinking.
**Dmitrii Anoshin** 25:52 If we have a default, it should be fine. And, I… we… I think we have an issue regarding… related to this. It was more generic, being able to Parametric or per group of metrics, specify like… Support, kind of.
requirements, availability in particular… based on particular external, environment, and that including OS support, but also, for example, in some let's say, MySQL receiver, for example, some metrics are available on the newer versions, but not available on the older versions, so that kind of field would have kind of, I don't know, like, conditioning, maybe?
Options, so, like, you can say version, smaller than something, or… OIS… equals, or something like that. If we can design it this way, that it can be generically applied to Other places, that would be perfect.
**Braydon Kains (Google)** 26:59 Yeah, that makes sense. I posed the issue where we last talked about this, it was, Damien suggested that maybe we adopt the pattern of, like, annotations, like Weaver has.
And that way we could introduce various types of annotations, such as requirements for enablement, like… like what you mentioned, and OS support could be one of them, and also there could be, like, version constraints or something. I don't know exactly How the… how that, specification Should work, like, maybe… the condition has a name, and when mDataGen Generates the code, the… the enablement function takes in some kind of… like… condition value that evaluates to true or false, that I'm… I'm not sure exactly how to do that yet, but…
**Dmitrii Anoshin** 27:53 Yeah.
**Braydon Kains (Google)** 27:54 That was… Our initial thought process.
**Dmitrii Anoshin** 27:56 Something like that.
**Braydon Kains (Google)** 28:04 That's on my list, I've just had to push it off for some other stuff first.
**Donal O'Sullivan** 28:14 So that would be a… would that be a runtime error? That'd be a generation time error, then, I guess, wouldn't it? What you want to do is a runtime error, so that you.
And then at runtime, if the config has the wrong metric, you just do the runtime error, is it?
**Braydon Kains (Google)** 28:26 That's the hope, yeah, and not a, like, collector failing runtime error, but, like, a warning to the user that we couldn't enable This piece of telemetry because of this constraint.
**Donal O'Sullivan** 28:41 Yeah, makes sense.
**Dmitrii Anoshin** 28:44 I posted the issue that I was talking about.
**Braydon Kains (Google)** 28:51 Got it. I will link these together.
**Dmitrii Anoshin** 28:55 Thank you.
**Braydon Kains (Google)** 28:59 Oh, hey, I commented on this last year. That makes sense.
Alright, yeah, I'll put these issues together, because they're kind of the same thing.
**Dmitrii Anoshin** 29:15 Cool.
controls.
**Braydon Kains (Google)** 29:18 Alright. See you next time. Have a good one.
**Roger Coll** 29:21 Oh, a wood one.
**Donal O'Sullivan** 29:21 Alright.
