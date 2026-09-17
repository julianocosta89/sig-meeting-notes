SIG: Zig SIG
Date: 2026-09-16
Duration: 45 minutes
============================================================

## Zoom Recording Transcript

**Francesco Gualazzi (OpenTelemetry)** 00:34 Hello, Antoine.
**Antoine Gagniere** 00:37 Hello.
**Francesco Gualazzi (OpenTelemetry)** 00:39 How you doing?
**Antoine Gagniere** 00:40 Right, and you…
**Francesco Gualazzi (OpenTelemetry)** 00:43 Not bad.
usual stuff.
**Antoine Gagniere** 00:49 Hmm.
**Francesco Gualazzi (OpenTelemetry)** 00:50 Definitely. Okay.
There's been a handful of PRs, enjoyed both from you and from new contributors, and so I'm very happy.
And, yeah, what I'm about to merge, also, it fixes the… The aggregation, the cumulative aggregation for, well, he still comes?
My… for leaving it like that, right?
I said, it's one of those to-dos that I said I should… I had, would have done in the future, and then… and forgot, okay, whatever.
Okay.
What's the, it's your, what's your take on the… the LTP. I want to talk about the LTP, so… I haven't had, any response from Laurent, the maintainer of,
**Antoine Gagniere** 01:51 Yep.
**Francesco Gualazzi (OpenTelemetry)** 01:52 And, yeah, the proposed, approach… in PR number 54 is not entirely… Not entirely bad. I agree that it should be fixed on the transport, But what if we… Because the project seems a bit difficult to… Mmm… rely on… Do you think if we find an alternative solution, such as that we… Encode and decode, ourselves.
**Antoine Gagniere** 02:34 Like, specifically for…
**Francesco Gualazzi (OpenTelemetry)** 02:37 Just for the trace and span IDs, yes.
**Antoine Gagniere** 02:40 Right, yeah. So, yeah, basically, we could merge the… PR as a workaround, right?
This is what you are proposing.
**Francesco Gualazzi (OpenTelemetry)** 02:49 Yeah, yes… I mean, the VR still contains some… some weirdness, such as, for example, there is a duplication of standard layover plaintext. You can see my comment here.
So, the PR needs to be reworked. I can take ownership of that and do the necessary changes, but… I was more asking your opinion… with regards to… Making this happen.
Not in the transport, and, let's say, on the… On the… on the encoding and decoding that we do on our side.
**Antoine Gagniere** 03:30 Hmm.
**Francesco Gualazzi (OpenTelemetry)** 03:32 Because Joseph… no, Joseph, Jacob's PR in Zig Brotov is big. It's massive, and the hex encoding is just one of them, right? Yes. It's one of the, one of the many things that he added there.
It's also been open for… mods, like…
**Antoine Gagniere** 03:55 Right, yeah.
**Francesco Gualazzi (OpenTelemetry)** 03:56 So, it's 3,000 line change that has been opened on June 5th.
And… the review is, is, dragging, yeah. I saw your approval, okay, but, And then there is a… oh, there has been a fix from Jacob, but… I don't know. I mean, we can wait, but it's… One more thing that piles up in the list of bugs, if you will, not compliant things that I wish we could get rid of, right?
**Antoine Gagniere** 04:41 Yeah, yeah, right.
**Francesco Gualazzi (OpenTelemetry)** 04:42 I don't know.
**Antoine Gagniere** 04:43 Yeah, well, we can, we can, because… because it is specific to a TRP, so it kind of makes sense to… to have a tier, yeah.
**Francesco Gualazzi (OpenTelemetry)** 04:52 Okay, and if we do the… in the PR, just like in Cheater, the contributors did.
What happens when, eventually.
Jacob's PR is merged upstream, and we have to upgrade. Do we have a test? Do I have… do I have to add a test?
That ensures that we don't do… Something weird with the wire format.
I guess?
**Antoine Gagniere** 05:19 I mean… Like, we could keep the test, right? Like, we just have to…
**Francesco Gualazzi (OpenTelemetry)** 05:32 No, we're… okay, yeah, but… Okay.
**Antoine Gagniere** 05:35 I mean, we could keep… the test that… the… Yeah, yeah, the… So… I think, yeah, I think it would not… Break anything if they merge?
the PR.
**Francesco Gualazzi (OpenTelemetry)** 05:54 Okay.
So… let's say that I will work on it, I will have… I will work on it this week.
Try to resume, I presume that we are… See what we can get out of it.
Because I want to get rid of that bug.
Right.
Yeah.
It's hitting, I mean, no, let me tell you, let me take a step back and tell you why I'm trying to fix as many things as possible.
We have had a… we've had a PR, huh?
Where's that?
I saw APR… no, yesterday, I saw an issue, a new issue.
came in that is referencing a PR Yeah, timeout set. Number 95.
This guy, this folk, is trying to… I mean, it's raising the fact that we have a bug in the timeout, which is also… I validated it. I remember why I did it like that.
Simply because the standard library HTTP client does not have any timeout.
And he's raising that this is a blocker, 4 is linked PR That is very interesting. So, the person here, Arnav, is adding opt-in opt-in telemetry traces to Vercel Labs FX, which is an agent harness that Vercel built a while ago, I don't know if you've heard of it.
**Antoine Gagniere** 07:46 I was not aware, and in Zig, in Zig.
**Francesco Gualazzi (OpenTelemetry)** 07:49 It's written in Zig, yes, it is written in Zig, so the man, or the woman, I don't know, Arnav, how he… what's his identification, but he created… let's… let's… they created this PR in FX repo.
linking to the fact that there is this blocker about us honoring the timeout, which is fair, I guess, I mean, it is correct. So, it's a nice signal, I… I actually… I say, stumbled for a second, but I'm okay. So, the gist of it is, there are some cool products being built with Zig right now.
Some of them are trying to use OpenTelemetry, so we should be able to provide a stable working library, right?
And, the hex format, the timeout, all of these little things.
I would rather not have them pile up.
And we have to chase a lot of bugs and fixes.
And… and I would prefer just having something stable. So, instead of waiting for the hex encoding, the coding to happen on the transport.
I would say, just, let's do it ourselves.
**Antoine Gagniere** 09:12 Yeah, makes sense.
**Francesco Gualazzi (OpenTelemetry)** 09:14 All right, so, end of story. I will resume this PR, so let me add it to the meeting notes here.
So, Francesco to resume PR to… X.
encode… Cold.
UX encode… There is… Slash span IDs.
This one.
Alright, so I will do this, and yeah.
We've discussed a bit about the open issues.
I haven't looked at your GRP CPR, but I was pleasantly Presently surprised.
by the assignment and the other thing, the RTMS Builder, I think the assignment is, can be merged.
I don't know if you pushed more changes to it, I'm just reading right now.
**Antoine Gagniere** 10:21 rename me?
Because I realized that the singer was French.
**Francesco Gualazzi (OpenTelemetry)** 10:27 Okay. Well, acceleration is also in English, where assignment is more like something that you are… tasked with.
**Antoine Gagniere** 10:36 Well, I was surprised to… find out that assination is an English word, but it does not mean that… it does not mean to assign, yeah.
So, yeah, I…
**Francesco Gualazzi (OpenTelemetry)** 10:47 There's a SIG fault in the macOS test.
We… what?
Yeah, the last change you did?
**Antoine Gagniere** 10:55 Cool.
**Francesco Gualazzi (OpenTelemetry)** 10:56 plugin macOS. Good.
**Antoine Gagniere** 10:58 point. Yeah, yeah, yes.
**Francesco Gualazzi (OpenTelemetry)** 11:00 I don't think it's nothing to do with your PR, though.
**Antoine Gagniere** 11:04 Maybe it does…
**Francesco Gualazzi (OpenTelemetry)** 11:06 Doesn't look like.
**Antoine Gagniere** 11:08 I mean, I'm surprised, because it previously didn't fail, and I just renamed.
But maybe my rename was… I don't know.
**Francesco Gualazzi (OpenTelemetry)** 11:16 Mmm… Is… is seg folding in a hash map?
In creating a Hashma.
**Antoine Gagniere** 11:26 Export background thread.
Would… Okay, okay, it's maybe not related to my PR, but.
**Francesco Gualazzi (OpenTelemetry)** 11:36 Definitely not, but it's…
**Antoine Gagniere** 11:38 investigate to… To have more… Like, if it's a bug, I would open an issue.
**Francesco Gualazzi (OpenTelemetry)** 11:46 Okay.
Looks like a bug on our side more than the… more than Zig, because it seems like simply that we are not initializing something.
at a capacity, Value iterator, the meter… well, how is this one fair? Collect?
Okay, I have to… I have to investigate this one, or you do that, but again, I don't think this is tied to your PR.
Also, why only on macOS?
That's weird.
I know, the test, no, they were canceled.
**Antoine Gagniere** 12:28 Yeah, the first one to fail, but…
**Francesco Gualazzi (OpenTelemetry)** 12:34 Alright.
Okay, I… don't know.
**Antoine Gagniere** 12:42 Yeah, we'll see. Okay, so yeah, so this one, I'm…
**Francesco Gualazzi (OpenTelemetry)** 12:47 This one is good. There's, Yeah, there's, the renaming you did, I haven't checked that, let me check.
And did you agree on also changing the… The generic, not the generic bandwidth, the subtyped, thing with, something more descriptive, instead of,
**Antoine Gagniere** 13:06 Right, yeah, yeah.
**Francesco Gualazzi (OpenTelemetry)** 13:07 assignment.
**Antoine Gagniere** 13:08 about it.
And so, yeah, maybe we can call it… Like, the generic one, just iterator, right? Or you…
**Francesco Gualazzi (OpenTelemetry)** 13:24 No.
**Antoine Gagniere** 13:25 Or…
**Francesco Gualazzi (OpenTelemetry)** 13:25 configure it, or a key value torett, or whatever, because again, what is this guy doing? The component here is… a, a component that… tries to parse… blocks… that are separated.
Buy something, right?
And the blocks are typically key value, but they could be anything, okay?
**Antoine Gagniere** 13:59 So… Yep.
**Francesco Gualazzi (OpenTelemetry)** 14:00 The generic one, the iterator, Looks good.
**Antoine Gagniere** 14:06 Yeah, so the not-generic one.
**Francesco Gualazzi (OpenTelemetry)** 14:09 The non-generic one, I mean, again, I would just say, comma qui value, whatever, because… That seems more logical, you know, because, again, you have an iterator. It iterates on what?
on comma-separated key values. And in this case, they are assigned with the equal.
Yeah. I saw…
**Antoine Gagniere** 14:35 So the not-generic one could be comma-separated as…
**Francesco Gualazzi (OpenTelemetry)** 14:39 I think I have a suggestion that says, comma step kV iterator, something like that, I don't remember, but the con… the idea is, yeah, Comma SEP kV iterate. The idea is… We have this generic struct that returns a subtype, that can do… Iteration on generic things that are separated by, by.
And then, this separated thing can be… assigned or not, right? There is also the case where it's only split, right?
Or no? No, because there is always a second parameter. Okay, never.
So… Again, iterator, for me, is fine, and then the subtype, I would say commasapKVER.
Or, comma, comma equal, kiwi, just to… just to understand, you know, from the name, what it does.
Do you see what I mean.
**Antoine Gagniere** 15:39 Yeah, yeah, so maybe the generic one, let me post a comment here…
**Francesco Gualazzi (OpenTelemetry)** 15:43 Yeah. Goes.
In the end, resource attributes are going to be comma separated, key values with a equal.
The trace… something… The trace state that Bach is adding, or maybe already added.
Oh, no, yeah, there's an open PR, which is also a long PR I'm reviewing that has a similar thing, so… This one will… will also…
**Antoine Gagniere** 16:11 Sophia.
**Francesco Gualazzi (OpenTelemetry)** 16:11 Yeah, the translator will also reuse it eventually.
So… Yeah, just, just to say, if we make… subtypes available that are easy to understand from the name, it's probably better.
**Antoine Gagniere** 16:32 Yeah, yeah, okay, okay, yeah, we'll name it Coma Separated.
**Francesco Gualazzi (OpenTelemetry)** 16:35 Okay.
**Antoine Gagniere** 16:36 Awesome.
**Francesco Gualazzi (OpenTelemetry)** 16:37 Other than that, I don't see… that's… that's the good stuff, actually. That's, some comp time, love.
**Antoine Gagniere** 16:47 Then second one is… attribute builder, what?
**Francesco Gualazzi (OpenTelemetry)** 16:55 Yep.
**Antoine Gagniere** 16:56 Mmm… Yeah, so the… For the in… yeah, there's two things to note here.
One is… Currently, the generated code Only generates a string values and enum values. Doesn't… like, for example, it does not… Say that, status should be a need.
**Francesco Gualazzi (OpenTelemetry)** 17:24 Hmm.
**Antoine Gagniere** 17:25 view string, which is not correct, but… it's, like, all is the generate… it's… is it Weaver that generates the code, or…
**Francesco Gualazzi (OpenTelemetry)** 17:36 Is it, it's Wave Affairs.
**Antoine Gagniere** 17:38 and so Weaver for Zig, who, who maintains.
**Francesco Gualazzi (OpenTelemetry)** 17:41 No, we have… I mean, Weaver is Weaver, and we built some, templates, Ginger templates, that generate the Zig code.
**Antoine Gagniere** 17:51 Okay.
**Francesco Gualazzi (OpenTelemetry)** 17:52 You can also modify them if you want. I mean, if you want to do… some… Added blocks that do comp time assertions, you can add them in the template.
Maybe also conditionally.
**Antoine Gagniere** 18:06 No, no, I mean, so premium attributes, string attributes… Okay, but what about integer attribute?
**Francesco Gualazzi (OpenTelemetry)** 18:17 Integer attribute, we have a needum for int attributes, yes.
**Antoine Gagniere** 18:23 Like, yeah, I'll, for example, so, let me look at, resource.zig, and… They're, like, they're all string attributes, right?
HTTP… What?
**Francesco Gualazzi (OpenTelemetry)** 18:55 You're sending me something in the chat?
**Antoine Gagniere** 18:57 No, I'm looking for,
**Francesco Gualazzi (OpenTelemetry)** 19:00 Right?
**Antoine Gagniere** 19:01 It's not in resource attribute… It's attribute.ig, not resources. Yeah, let me share my screen, maybe I will.
**Francesco Gualazzi (OpenTelemetry)** 19:07 Yeah, please.
**Antoine Gagniere** 19:13 So, here, I'm going to look for HTT.
Made food.
You know, like, requests.
Size, like, yeah, size… It should be nit, right? But so… but it's declared string attribute.
We cannot do come-time magic to validate.
**Francesco Gualazzi (OpenTelemetry)** 19:43 Okay.
**Antoine Gagniere** 19:44 Right here. So I can do it for… for, in your address.
**Francesco Gualazzi (OpenTelemetry)** 19:50 Yeah.
**Antoine Gagniere** 19:51 And as you see, the enumer tribute has.
**Francesco Gualazzi (OpenTelemetry)** 19:54 But do you know why it's a string, probably?
Cause the size is, You know, one of those, humanized, measures, like, 128 key…
**Antoine Gagniere** 20:09 Oh, but what was status code? It should be a need.
**Francesco Gualazzi (OpenTelemetry)** 20:13 Yes, but… It should be response, that was called? Yes, it should be an int, I don't know why it's string. There's a way of checking… I mean.
The reason why this is a string, it comes from the YAML.
Right? So…
**Antoine Gagniere** 20:31 Yeah, where is this YAML?
**Francesco Gualazzi (OpenTelemetry)** 20:33 Inside, spec, I believe? Where is that?
into this… SMCOM, yeah?
There's a YAML config somewhere… But over here, this is the build folder, down in the… yeah, in the open telemetry Sandconv.
**Antoine Gagniere** 20:57 Yeah, but I mean, the… It's…
**Francesco Gualazzi (OpenTelemetry)** 21:01 You are in the build folder, okay.
Yes, good evening, sir.
**Antoine Gagniere** 21:04 How do we…
**Francesco Gualazzi (OpenTelemetry)** 21:07 Not here, this is the build folder.
**Antoine Gagniere** 21:09 Yeah, but who generates the…
**Francesco Gualazzi (OpenTelemetry)** 21:12 Yeah, okay, here in source… And in scripts, okay, the template…
**Antoine Gagniere** 21:20 Where do they get the…
**Francesco Gualazzi (OpenTelemetry)** 21:22 This is the script that, checks out the… The repo?
Yep.
**Antoine Gagniere** 21:29 So here, I'm guessing that it's here. I should.
**Francesco Gualazzi (OpenTelemetry)** 21:32 Yes, yes, yeah. You have to go into schemas, if I'm not mistaken? No, it's not this one. Go into model… Yes? HTTP.
**Antoine Gagniere** 21:45 model? Oh, okay.
**Francesco Gualazzi (OpenTelemetry)** 21:47 Yeah, yeah, that's… I think so. I remember. Yeah, I see it.
And then you take the… I think that's Matrix?
Status code, or registry? Take the registry.
Yeah.
Here, you should find .status.code.
**Antoine Gagniere** 22:08 And, here we have attributes… Of a span, yeah.
**Francesco Gualazzi (OpenTelemetry)** 22:13 No, this is for the span. We use only registry, if I'm not mistaken.
**Antoine Gagniere** 22:19 But what does it mean? Okay.
**Francesco Gualazzi (OpenTelemetry)** 22:23 So the registry is the list of all, things, and it has a type. Okay, HTTP response size type int, so yeah, we should…
**Antoine Gagniere** 22:31 I pinned.
**Francesco Gualazzi (OpenTelemetry)** 22:33 Okay, then there's something wrong in our templates.
**Antoine Gagniere** 22:36 So I'm guessing it's the generator itself that we use, that also only supports… yeah, yeah.
**Francesco Gualazzi (OpenTelemetry)** 22:44 I… don't… I have to check. Last time I checked, it was working also for great, but, yeah, please, create a… create an issue, otherwise I can create it for the same converse stuff that,
**Antoine Gagniere** 22:59 Okay, good.
**Francesco Gualazzi (OpenTelemetry)** 22:59 We should… that he should be… should be honorable, yes.
**Antoine Gagniere** 23:03 So, shoo… Simcoe… attribute… And yeah, I can link maybe to this… Hmm… Really?
Hmm.
Okay, yeah, maybe, we could… I would rewrite… Better after better.
**Francesco Gualazzi (OpenTelemetry)** 24:03 Yeah, yeah, I'm also writing a new issue for the metrics.
There we go. Save.
**Antoine Gagniere** 24:12 Okay, so…
**Francesco Gualazzi (OpenTelemetry)** 24:14 Matrix.
**Antoine Gagniere** 24:15 So, yeah.
**Francesco Gualazzi (OpenTelemetry)** 24:18 Anyone.
**Antoine Gagniere** 24:19 because there is this limitation, I cannot check the type of the value, except when it's an enum.
And then, in this case, that's why it's possible to… to do this… Well, I'll just say .get without… Saying the type, and it, it gets, basically, yeah, from the known… well-known values.
And yeah, I wanted to ask a question about this, is, when I go back to SEMCOM… source attribute.
And, so, yeah, this one is,
**Francesco Gualazzi (OpenTelemetry)** 25:04 But I think this is also… this is generated as well.
**Antoine Gagniere** 25:07 Yeah, yeah, it's all generated, right? So the NUM attributes, they have these well-known values with an S, But what they always do is they give only one value.
But it's okay for me, because from one value, I can do type of, and I get the type, so I… found this enum, because I do type off of the.
**Francesco Gualazzi (OpenTelemetry)** 25:31 No, yeah, okay. So that one is an enum, it's not, literal.
**Antoine Gagniere** 25:36 Yes, he's an idiot.
But… Like, when…
**Francesco Gualazzi (OpenTelemetry)** 25:41 No, I did. Okay.
**Antoine Gagniere** 25:43 well-known values… Could be a list of values.
Or should it be only one example of a value?
**Francesco Gualazzi (OpenTelemetry)** 25:53 No, I think it should be pointing to the enum, I guess.
Because all the, all the variants of the enum are valid, well-known variants.
**Antoine Gagniere** 26:03 Yes, yeah.
**Francesco Gualazzi (OpenTelemetry)** 26:05 But now it's pointing only to one.
**Antoine Gagniere** 26:07 So, yeah, yeah. So, I'm guessing if we have to, we can just fix this template, I guess, and we… Remove the… the…
**Francesco Gualazzi (OpenTelemetry)** 26:16 Okay.
**Antoine Gagniere** 26:17 handled, so then I would just need to edit my PR, right? Because currently, I'm doing type of well-known value, but I can now just take the… Take itself.
**Francesco Gualazzi (OpenTelemetry)** 26:30 Yeah, yeah, yeah.
**Antoine Gagniere** 26:31 the type, yeah. So that's good, yeah, and so… Yeah, currently I do not check the string and ints, because we're not sure.
Yeah, that's it.
**Francesco Gualazzi (OpenTelemetry)** 26:49 Okay.
**Antoine Gagniere** 26:50 Mmm…
**Francesco Gualazzi (OpenTelemetry)** 26:51 This is super cool, by the way.
**Antoine Gagniere** 26:53 Yeah, thank you.
Yeah, so this, you are right, it does not need to be pub, so I will remove…
**Francesco Gualazzi (OpenTelemetry)** 27:00 Okay.
**Antoine Gagniere** 27:00 move it.
**Francesco Gualazzi (OpenTelemetry)** 27:02 You see, this is a sign that I don't review my PRs using AI, because I read the entire code and reason on what's happening.
**Antoine Gagniere** 27:12 Yeah, yeah, correct. But in this case, I don't even think it's… Even though it is probably… it's not accessible.
from outside, because… Okay.
**Francesco Gualazzi (OpenTelemetry)** 27:23 Eyes not declared. Okay.
**Antoine Gagniere** 27:25 Here, it's… What's actually available is this?
**Francesco Gualazzi (OpenTelemetry)** 27:33 We don't export the whole file, yeah, yeah.
**Antoine Gagniere** 27:36 It's re-exported, so yeah.
We do not have access to…
**Francesco Gualazzi (OpenTelemetry)** 27:40 Okay.
**Antoine Gagniere** 27:41 But yeah, yeah, you're right. Okay, so this was one PR.
And this one… Yeah, we have the two last one, yeah, so the GRPC one… was, from, you know, from March or April.
Hmm.
**Francesco Gualazzi (OpenTelemetry)** 28:02 Hi, this is the updated version, the new repo of the same that you opened on Zig Observability.
**Antoine Gagniere** 28:08 Yeah, yeah, like, I opened… when the… yeah, in March, I opened the first one, and then it was too complex, so I split it in two. Okay. So, we've merged the first one now, and…
**Francesco Gualazzi (OpenTelemetry)** 28:18 Yeah, the option. Second one.
**Antoine Gagniere** 28:20 So it, it worked, but the, the AI has, has made some good points, but mistakes,
**Francesco Gualazzi (OpenTelemetry)** 28:30 Okay.
**Antoine Gagniere** 28:30 Which one? So, I need to address the comments of the AIC.
Before it can be munched.
**Francesco Gualazzi (OpenTelemetry)** 28:36 So Copilot is being useful. For me, this is something new, honestly.
**Antoine Gagniere** 28:41 Yeah, it's…
**Francesco Gualazzi (OpenTelemetry)** 28:43 Apparently, they improved it, so I have used Copilot 2 years ago, 1.5 years ago, I don't remember that. Definitely more than one year ago, and it was… terrible. Like, he was hallucinating all the time. But now, it seems that he's doing meaningful, reviews, so thanks, Copilot.
**Antoine Gagniere** 29:04 Yeah, yeah, b- That's strange. So, my understanding is that it's the… OpenTelemetry organization that pays for it. Nice. But we request it, so…
**Francesco Gualazzi (OpenTelemetry)** 29:18 It's the alternative to balanced, I see a drop-down there.
**Antoine Gagniere** 29:21 Yeah, yeah, it can be light.
**Francesco Gualazzi (OpenTelemetry)** 29:24 Okay.
**Antoine Gagniere** 29:25 So, for lower cost. Just, in this case, it's a complex PR, so I… Yeah, that's.
**Francesco Gualazzi (OpenTelemetry)** 29:30 Oh, yeah.
**Antoine Gagniere** 29:32 Yeah, it's… so what did it find?
**Francesco Gualazzi (OpenTelemetry)** 29:36 Yeah, which is…
**Antoine Gagniere** 29:40 completely true, and I even… I mean, yeah, I even wrote it in the comments, so it's… But… Because, like, to know if it's restable or not, it would require to… To do more, like, to pass traders?
And… okay, so this one is easy because it's written in a comment, but… He wants this… it wants it to not be retried by default.
Maybe, yeah, makes sense.
Yeah, I think it was… what already, it was mostly, right, so I think we have to address those.
So, okay, and the last one is an old PR from previous repo.
**Francesco Gualazzi (OpenTelemetry)** 30:34 Yep.
**Antoine Gagniere** 30:35 That I've modified,
**Francesco Gualazzi (OpenTelemetry)** 30:39 Oh, you've updated this one? Okay, I will, re-review.
Okay, no, you need to interact earlier, that's why it's still open, okay. Yeah, I remember that, okay, now I remember.
Alright, that's good for you.
**Antoine Gagniere** 30:51 Yeah, waiting on the turtle, so…
**Francesco Gualazzi (OpenTelemetry)** 30:53 As soon as the territor gets updated, I will approve, and then I will review the gRPC one also.
**Antoine Gagniere** 31:00 Yeah, yeah, okay, maybe I have a… I mean, gRPC1, you can wait for me to address the AI.
**Francesco Gualazzi (OpenTelemetry)** 31:09 Yeah, yeah, yeah, but I will still look at it, even if Copilot, I viewed, because I… you know, at least, you know, on the surface, I want to understand what it's doing, and how… And now it's affecting, the overall, Statue of the library, yeah.
**Antoine Gagniere** 31:28 But if you want, we can quickly go over it.
**Francesco Gualazzi (OpenTelemetry)** 31:31 Yeah, sure.
**Antoine Gagniere** 31:32 So… what?
Oding… Yeah, I've added…
**Francesco Gualazzi (OpenTelemetry)** 31:40 This is an example.
**Antoine Gagniere** 31:41 Yeah, those are examples I did.
**Francesco Gualazzi (OpenTelemetry)** 31:44 contest, huh?
**Antoine Gagniere** 31:45 So, what's important? Yeah.
Here.
What's important, so… This should be done only once.
**Francesco Gualazzi (OpenTelemetry)** 31:56 Oh, yeah.
**Antoine Gagniere** 31:56 Lifetime of the program.
**Francesco Gualazzi (OpenTelemetry)** 31:58 So, we are using the same, say.
behavior as HTTP Proto, where on every export call, we create a new client, and we then destroy it, right?
**Antoine Gagniere** 32:15 Exactly, yeah.
**Francesco Gualazzi (OpenTelemetry)** 32:16 Okay, so there's gonna be a refactor later on where we instead create this, say, transport, and we can swap the underlying, Thing, right?
**Antoine Gagniere** 32:26 Yeah, yeah, exactly, yeah. So, yeah, this would be not… need to be done only once, but this would be… Could the endpoint change in time? No, I don't think so.
**Francesco Gualazzi (OpenTelemetry)** 32:41 Winter of what?
**Antoine Gagniere** 32:43 the… Yeah, the IP you are targeting is not.
**Francesco Gualazzi (OpenTelemetry)** 32:50 Total pinpoint. I…
**Antoine Gagniere** 32:55 It's fixed once you start, right? You can modify.
**Francesco Gualazzi (OpenTelemetry)** 32:58 Yes, I mean, it could be reloaded at runtime, but…
**Antoine Gagniere** 33:03 Oh. I mean…
**Francesco Gualazzi (OpenTelemetry)** 33:03 Nothing that is… I mean, for what this one is concerned, it should always read it from configuration.
So…
**Antoine Gagniere** 33:13 Okay, yeah.
then credentials.
**Francesco Gualazzi (OpenTelemetry)** 33:17 Oh, no.
**Antoine Gagniere** 33:17 For now, we don't, yeah, but… Then the core, hmm… Yeah, no, in this case… yeah, in this case, I think there's nothing that… Needs to be… it's all once globally.
**Francesco Gualazzi (OpenTelemetry)** 33:34 What is… what is the plaque, Q? Can you explain?
**Antoine Gagniere** 33:38 So, the, the… gRPC is quite complex, so to do the most basic thing, which is just send a message.
That is not a stream, so we… you still need to Build all those objects, and so you need the cube.
The… and this… multiple types of queue.
And the plug queue is mean… it means that it can hold multiple types of events, and when you want to Take the last events, because it's a queue, the… the… It's a queue, so not the last one, but the older, oldest one, yeah.
You… Give the type.
And it will only pick of this type, and so it means… Yeah, you do not get the oldest one, you get the oldest one of the type that you want.
**Francesco Gualazzi (OpenTelemetry)** 34:40 Okay.
**Antoine Gagniere** 34:41 In this case, I really don't need something that complex.
**Francesco Gualazzi (OpenTelemetry)** 34:45 It's like a sorted harsh mutt.
**Antoine Gagniere** 34:47 Mmm… Yeah, possibly… It's, like, a hash map of queues.
Yeah, I'm not even sure, so… Here, make the call, and then what?
Yeah, because here, here I use a raw near a record, which is quite, high level.
**Francesco Gualazzi (OpenTelemetry)** 35:19 UNAV is fine, I mean, I guess… I think even the… The Go SDK uses UNAC, so that's perfect.
**Antoine Gagniere** 35:27 Yeah, no, you, you know, I mean, that… Usually, with a channel, you create code… no, sorry, I mean… queue… so, yeah, a queue… Pluck queue, you plug, and the next queue…
**Francesco Gualazzi (OpenTelemetry)** 35:55 I don't hear you anymore.
S… Do you hear me?
**Antoine Gagniere** 36:06 Yes?
**Francesco Gualazzi (OpenTelemetry)** 36:07 Okay, now we do, okay.
**Antoine Gagniere** 36:11 And so, what I wanted to show is… So… Batch, oh yeah, when you have a batch, you start the batch.
And yeah, so this rawinary call function, this high-level helper that I made especially for the Zig SDK, which… Those, in one call… The multiple things you would need to do manually, so…
**Francesco Gualazzi (OpenTelemetry)** 36:51 Okay…
**Antoine Gagniere** 36:52 You create a call from the channel, Then you create a batch.
You place one message to send as a badge, you tell the badge that you expect a reply for this message, you start the batch.
Then you wait from your queue.
And… woo-woo… So we don't.
**Francesco Gualazzi (OpenTelemetry)** 37:19 For as long as that, right?
**Antoine Gagniere** 37:21 And, yeah. And then… if it… Succeeds…
**Francesco Gualazzi (OpenTelemetry)** 37:28 It does return the success with the bytes.
**Antoine Gagniere** 37:31 Right? But it means we did not pluck. So, wait, wait, wait, I don't remember this one, so Q… Wait… Oh, there's no way to… sorry, oh, we're not waiting… waiting on the queue.
We're waiting on the batch, yeah, correct. And so batch, wait… It plugs, yeah, okay, yeah, yeah, that's it, I found. Okay.
So, because I did a trick.
**Francesco Gualazzi (OpenTelemetry)** 37:59 Okay.
**Antoine Gagniere** 38:00 So what was the trick, exactly?
**Francesco Gualazzi (OpenTelemetry)** 38:05 I think your audio disappeared again.
Don't know why.
Now you're back.
**Antoine Gagniere** 38:21 Huh.
Okay.
Yeah, yeah, well, anyway, just that… We… we need to plug Q… It'd be cool.
**Francesco Gualazzi (OpenTelemetry)** 38:42 This looks readable, I guess, yes.
**Antoine Gagniere** 38:47 Yeah, yeah, it's been a while, so sorry, a bit forgotten.
**Francesco Gualazzi (OpenTelemetry)** 38:50 That's okay.
**Antoine Gagniere** 38:51 But I remember that I…
**Francesco Gualazzi (OpenTelemetry)** 38:52 I can see what's happening here, right? So… You create the batch in the Euro Unicorn.
**Antoine Gagniere** 38:59 Yes, exactly.
**Francesco Gualazzi (OpenTelemetry)** 39:00 Then you fill the batch with the data that you are passing In, as a parameter.
And then you wait for the message to land?
Oh, no, expect received message is… before you… Send the batch, okay? Then you send the batch, and then you wait for the batch to complete, which involves consuming the channel and actually sending the data over.
**Antoine Gagniere** 39:29 Yep.
**Francesco Gualazzi (OpenTelemetry)** 39:30 Okay? You too.
And we are returning Rocular.
That is mirroring the… Batch weight arrows that you can see there, okay.
**Antoine Gagniere** 39:46 Yeah, the roll call… let's check the roll call error, we'd… Oh, cool.
Oh, yeah, batch error, or… Wait, okay.
But… Bitch, bitch, bitch.
Well, I'm, in Bat Show, which retail.
But error is actually usage error.
And then we said, wait till… Well, yeah, define the waiter?
Oh, we do.
**Francesco Gualazzi (OpenTelemetry)** 40:34 Sadow of you, yeah.
**Antoine Gagniere** 40:35 Or… Q shut down.
And we should…
**Francesco Gualazzi (OpenTelemetry)** 40:39 Okay, so timeout, out of memory, no inbound message expected.
Okay.
Where does that timeout come from, then? Dot timeout?
**Antoine Gagniere** 40:52 Yeah, so the timeout is, deadline, right? So we would just.
**Francesco Gualazzi (OpenTelemetry)** 40:58 Excited.
**Antoine Gagniere** 40:59 the deadlines.
**Francesco Gualazzi (OpenTelemetry)** 41:00 It's water… okay, because there is a try, I see, okay.
Nice, okay.
**Antoine Gagniere** 41:06 Yep.
So… Yeah, yeah, so, and so the thing is, when you get a queue.
Like, they made it very complex, and in theory, you should be able to use one queue for multiple batches at the same time.
**Francesco Gualazzi (OpenTelemetry)** 41:30 You mean for multiple RPCs?
Or for multiple messages.
**Antoine Gagniere** 41:36 like, multiple… well, multiple batches, so I… yeah, that can contain a message.
But I'm not doing that here, so I'm using only one cube.
**Francesco Gualazzi (OpenTelemetry)** 41:52 Yeah, yeah.
**Antoine Gagniere** 41:52 Per… cool.
which means… The proc queue is not necessary, but… I'm making… trick, so I mean, the tag, now, in theory, can be an arbitrary value. You could put any value on the tag, so it's like an integer. You can put… But what I do is I put the pointer to… To the instance, adds a tag.
Which is a trick to… and so that's when I didn't use a plug queue, so I… like, here, yeah, you can see that I plug, and as a tag I use, Point to cast.
of self, so the address of the batch, I use it as a tag.
**Francesco Gualazzi (OpenTelemetry)** 42:45 Okay.
**Antoine Gagniere** 42:45 So I'm not sure what other gRPC users are supposed to do here, but, yeah.
**Francesco Gualazzi (OpenTelemetry)** 42:54 Me neither, I mean…
**Antoine Gagniere** 42:56 Yeah, I have no idea, so… but I did it, like, that way, because… Before, like, you're supposed to separate, like, you create the batch, you start it, and then you wait on the queue, and you don't remember what batch you were doing, like… So it forced the caller to give you the batch here, and then give you the batch And so it's, like, duplicating the… I found it, not as user-friendly, so I… yeah.
**Francesco Gualazzi (OpenTelemetry)** 43:28 That, this looks fine.
as long as we don't have to mess with the… with the transport and the data frames directly, I think this is… Just great.
Okay, very good.
Looking forward to… to that, also, landing, and testing it out, because… Last time that I tested, the… with a real auto collector, a Zig program generating data, I was happy, and if I can manage to also send via gRPC, that's gonna be fire.
**Antoine Gagniere** 44:09 Well, my… I did the test in March, and I used my, like, betadoc Yeah, right, and so I… and then I saw the data appear on Datadog, so it works end-to-end, so I… I know it works end-to-end, just this, some improvements to be made, I guess, Bill.
It does work into it, so…
**Francesco Gualazzi (OpenTelemetry)** 44:30 That's great. Awesome, Antoine. Great work here, I… This must be praised somehow.
**Antoine Gagniere** 44:38 Did you…
**Francesco Gualazzi (OpenTelemetry)** 44:39 I guess this, you know, because all the building blocks that we need to work with Protobuff, Zig Protobuff, this gRPC wrapper, those are essential things, essential components to the SDK.
Yeah. For what… for what the real workload that the people use in production is today. So if… if a service today that is written in Zig wants to onboard OpenTelemetry.
you know, gRPC protobuf is the standard, and if we don't offer a complete solution for that, the SDK is just difficult to use, huh?
**Antoine Gagniere** 45:17 Right, yeah, yeah.
And, by the way, so… I just thought about… so Protobuf is used for HTTP, like, protobuf over HTTP, right?
**Francesco Gualazzi (OpenTelemetry)** 45:31 Yes?
**Antoine Gagniere** 45:32 if we were to just use JSON over… HTTP, then we don't need portables, right?
**Francesco Gualazzi (OpenTelemetry)** 45:40 we can do… we already do HTTP JSON.
**Antoine Gagniere** 45:43 Yeah.
**Francesco Gualazzi (OpenTelemetry)** 45:44 With the caveat of the hex encoding of TracyDespan ID.
That one is broken, but that works already.
**Antoine Gagniere** 45:52 like, we could even have less runtime dependencies, right?
**Francesco Gualazzi (OpenTelemetry)** 46:00 Yeah, but the OTLP with HTTP JSON has been working fine since, I guess, before migrating to OpenTelemetry, because Jacob already had fixed that, in Zig Protobuff. There was, there was something that we fixed in Zig Protobuff.
Also, but, since then, I guess… both HTTP Proto and HTTP JSON, let aside the hex encoding, are just fine.
**Antoine Gagniere** 46:33 Yeah, yeah, yeah.
I mean, we… I was thinking… about… like, you know, gRPC is, like, optional dependencies, right?
**Francesco Gualazzi (OpenTelemetry)** 46:46 Yep.
**Antoine Gagniere** 46:48 And so, for someone that doesn't care about gRPCs, they disable it, and then they have a smaller… like, very small SDK, right?
**Francesco Gualazzi (OpenTelemetry)** 46:58 Yep.
**Antoine Gagniere** 46:59 And we…
**Francesco Gualazzi (OpenTelemetry)** 47:00 You wanna do the same with Portovac?
**Antoine Gagniere** 47:02 It's what they would say.
**Francesco Gualazzi (OpenTelemetry)** 47:04 You mean, like, using it as a lazy dependency?
**Antoine Gagniere** 47:10 like, where… is it the right dot zone, or… I mean…
**Francesco Gualazzi (OpenTelemetry)** 47:16 Zig Zone, no?
**Antoine Gagniere** 47:18 Yeah, it's alright… I mean…
**Francesco Gualazzi (OpenTelemetry)** 47:21 Use that.
**Antoine Gagniere** 47:22 Could, we only need it… like, we could disable it at runtime, like, I mean, not at runtime, but not use it at runtime.
**Francesco Gualazzi (OpenTelemetry)** 47:35 Oh…
**Antoine Gagniere** 47:36 just HTTP and JSON.
**Francesco Gualazzi (OpenTelemetry)** 47:38 Okay, you mean if someone is not… compiling… the OTLP… HTTP protobuf.
support, so compile without HTTP protocol support or gRPC protocol. Only compile with HTTP JSON support.
Okay, yes, although I don't see the big advantage, because…
**Antoine Gagniere** 48:06 You know, maybe that's a bad idea, yeah.
Yeah, I was thinking, like, if someone would want to re… like, get the smallest binary possible, but… Maybe that's not a good…
**Francesco Gualazzi (OpenTelemetry)** 48:19 It could… it could be done, but yeah, I don't see it as a… problem, or something that we should focus on right now, honestly.
**Antoine Gagniere** 48:26 Right, right, right, yeah, yeah, no, correct.
**Francesco Gualazzi (OpenTelemetry)** 48:30 Okay.
**Antoine Gagniere** 48:31 Yep.
**Francesco Gualazzi (OpenTelemetry)** 48:33 Nice, thanks for the thorough review.
I… I don't have anything else, and I can give you back 10 minutes if you want to take a break from today. Oh, I think as your day is almost over, no?
You're working days.
**Antoine Gagniere** 48:53 Yeah, yeah, yeah, it is over, right? Yeah.
**Francesco Gualazzi (OpenTelemetry)** 48:56 Nice. Awesome.
We will see you in two weeks.
**Antoine Gagniere** 49:00 Yep.
**Francesco Gualazzi (OpenTelemetry)** 49:02 Thank you, Antoine. I… I will go back to my reviews and be… As fast as possible in keeping your pace.
**Antoine Gagniere** 49:11 words.
**Francesco Gualazzi (OpenTelemetry)** 49:13 Enjoy the week!
**Antoine Gagniere** 49:14 Yep, see you.
**Francesco Gualazzi (OpenTelemetry)** 49:15 Cheers. Bye.
**Antoine Gagniere** 49:16 But…
