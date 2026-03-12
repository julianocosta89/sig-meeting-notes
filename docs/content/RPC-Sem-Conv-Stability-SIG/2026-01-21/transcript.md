SIG: RPC Sem Conv Stability SIG
Date: 2026-01-21
Duration: 50 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:56 Dear Bogdan.
Please.
Don't send your meeting notes.
We have recordings out there, and we do not authorize you to use Our meanings.
We have a new bot, Trask?
**Trask Stalnaker** 01:22 Hello, new bot.
I told it that we don't like it.
We don't… we do not consent.
**Liudmila Molkova** 01:31 We did not, no.
**Trask Stalnaker** 01:33 Opt, out, read, type, read, stop, oh… What is that? Read stop.
Oh, that's… that's a nicer bot. Much nicer, more polite bot.
**Steve Rao** 01:48 Hello?
**Trask Stalnaker** 01:49 It tells… it gives you, like, you can actually… You can actually, disable it just by typing to it.
**Liudmila Molkova** 01:59 Did you… what did you tell it?
**Trask Stalnaker** 02:03 Do you see its message to… did it… oh, did it give you a private message?
**Liudmila Molkova** 02:09 It is a private message, yes, so did you say read, stop, or did you.
**Trask Stalnaker** 02:13 I did, I typed… Oh, to delete, meaning opt out? I said read stop.
**Liudmila Molkova** 02:19 Okay, I said opt out. Last time I did read stop, and nothing happened. Now I did opt out, and it disappeared.
**Trask Stalnaker** 02:27 Oh, okay. I did read stop, and it disappeared too, so I don't know which one… maybe your opt-out worked and not… I thought my read stop…
**Liudmila Molkova** 02:37 I'm sure we'll have a chance to test it more.
**Trask Stalnaker** 02:39 The attested… exactly, exactly.
**Liudmila Molkova** 02:49 Cool, so let's get started!
Consolations… this is… 21st and 22nd… Let's see… what do we have on the triage board?
Okay, quite…
**Trask Stalnaker** 03:18 down there.
**Liudmila Molkova** 03:20 Yeah.
So… nothing new that needs triage.
Nothing in to-do that's sectionable?
And a lot of things in progress.
**Trask Stalnaker** 03:45 Oh, let's… yeah, let's go through those.
**Liudmila Molkova** 03:49 So this… It's our two friends about the GRPC.
And it has the last blocker that I want to chat more about.
Right. So this is probably… You approved Trask, but I realized it had a problem, so maybe we should talk a little bit about it.
**Trask Stalnaker** 04:11 Yeah, yeah, I saw your comment.
**Liudmila Molkova** 04:17 Okay, so… Let's figure out this one first, and then, the mapping is just a question of review, there is nothing to discuss, really.
**Trask Stalnaker** 04:30 Sounds good.
**Liudmila Molkova** 04:32 so, we have migration doc, this difference.
**Trask Stalnaker** 04:40 What's this one? Review metric requirement levels?
**Liudmila Molkova** 04:47 Oh, I think we can remove it from our board.
You sent a PR, right, and it emerged.
**Trask Stalnaker** 04:55 Yeah. Okay, perfect.
Gone… If I figure out how… Okay.
Yes.
**Liudmila Molkova** 05:19 Okay, I think we should, take a look at Apache double today.
Thanks a lot, Steve, for sending it.
**Steve Rao** 05:28 Yeah, no problem.
**Trask Stalnaker** 05:35 Did you have a chance yet this morning to see Lyudmila's comments?
**Steve Rao** 05:40 Yeah. But, but I, I don't think, fix them.
Is it…
**Trask Stalnaker** 05:47 Is there anything that you want to talk through that you're not totally clear on?
**Steve Rao** 05:51 Yeah, maybe about the status code. Yeah, maybe we can discard later.
Yeah, because in double 2 and double 3, the static code is totally different, the format.
But, yeah, so far, I just list some status code, in W2.
**Liudmila Molkova** 06:16 Okay, let's talk about it now. I don't think we have much else to go on the board.
So, this… we are going to… We are defining conventions for double Survey, right?
**Steve Rao** 06:32 yeah, if I remember right, yeah, at first, maybe, Yeah, maybe we discard, maybe we can start from W2.
**Liudmila Molkova** 06:48 So you…
**Trask Stalnaker** 06:48 One is Alibaba, Bobo 2 is Apache.
Is that right?
**Steve Rao** 06:54 yeah.
**Trask Stalnaker** 06:58 And 003… is…
**Steve Rao** 07:04 Yeah, it's also Audible… it's also Apache.
**Trask Stalnaker** 07:07 Okay.
**Steve Rao** 07:11 But, I can share, documentation about, state codes in double 3.
**Liudmila Molkova** 07:24 Yeah, I sent a…
**Steve Rao** 07:26 I have link in China.
**Trask Stalnaker** 07:31 Is 002 still… Kind of the default… Or, oh no, I see it, triple is the…
**Steve Rao** 07:40 How about sweet.
**Trask Stalnaker** 07:42 Okay, got it. And that link points to TCP, okay.
**Liudmila Molkova** 07:52 So this is… these are the… error quotes and their HTTP on their parts.
**Steve Rao** 08:00 Yet, yeah, the… The end of… this, part is gRPC, yeah, 33 is extended gRPC protocol, so it uses gRPC, status. Yeah, you can, scroll down.
**Liudmila Molkova** 08:16 Whoa.
**Steve Rao** 08:16 of all that.
**Liudmila Molkova** 08:19 You can scroll down. Yeah, there is a mapping.
**Steve Rao** 08:23 From double, statical to… Yeah, you can see the little one. Stat code to JRBC status.
Oh, this one.
**Liudmila Molkova** 08:36 Yeah. I, I, I see. So, it can be… Either the gRPC or… one of this?
**Steve Rao** 08:51 Yeah, but I think, yeah, maybe it's, Yeah, main use case is, the latter.
it's an extended gRPC, but the HDP just, compatible protocol.
**Liudmila Molkova** 09:09 Okay So then, okay, so maybe, when we are defining this pan, this is for… The report.
Exjitor.
Or it's, it's agnostic, it can be about either of them.
**Steve Rao** 09:28 Yeah, yeah, so, so far, yeah, at least it's, W2, state code.
It's a, it's a different, Format, set code compared with double 3.
**Liudmila Molkova** 09:50 Yeah, so should we update the status codes, or should we mention that it's for W-2? And do we even want to document W-2?
**Steve Rao** 10:02 Yeah, I think it's fine. Yeah, maybe we can mention that.
But I'm not sure how to, document them together in our semantic convention, such as, maybe we say this is a double 2 static code, and another one is a static code from double Z.
Yeah, is there any case in our previous semantic convention to solve similar, scenarios?
**Liudmila Molkova** 10:37 Tons?
**Trask Stalnaker** 10:38 of any, but I don't see a problem with just free-form note… say, for 002, this is the… this is the set of status codes. For 003, this is the set of status codes.
**Steve Rao** 10:55 Okay, yeah.
**Trask Stalnaker** 10:58 I mean, we can get more fancy in the future, potentially, and split out separate span definitions for them if we wanted to.
But I… Don't think that, I think just free-form text.
Would be fine for stabilization.
Is there anywhere else that we need to call out the difference between 002 and 003?
**Steve Rao** 11:34 Hmm… Yeah, just that quota is the, yeah, first part. And, another one is, maybe, is, Protocol information.
Yeah, in W2, it's based on TCP, and double 3 is, yeah, it's extended gRPC protocol called Triple.
**Liudmila Molkova** 11:59 Oh, so, let's take a look here… What attributes do we actually have?
Network, yeah.
So, like, you can, reference the protocol name version.
And you can say, okay, this is… you can modify Not sure if brief is interesting to modify, but for example, you can modify this example to be And what do you call it, triple?
**Steve Rao** 12:35 Okay.
Oh, wait, is it…
**Liudmila Molkova** 12:39 No, it's not PayPal, right?
the… gRPC would not have gRPC here.
**Steve Rao** 12:51 Okay, you mean… yeah, in gRPC, which value we, fell with here?
**Liudmila Molkova** 13:02 Network protocol name.
Remember, we talked about it.
point.
A long time ago.
Okay, this is what we…
**Steve Rao** 13:38 Yeah, this card.
**Liudmila Molkova** 13:39 Discussed at some point.
Okay, so this is assuming logical.
Yeah.
**Trask Stalnaker** 14:01 Our GRPC for network protocol name, we're using HTTP.
**Liudmila Molkova** 14:29 And… Duh… I remember some discussions that fret up, but… There was some difference between Oh, all of them would be TCP, right? The transports would be TCP.
**Steve Rao** 14:47 The W2 is, yeah, it's based on TCP.
**Liudmila Molkova** 14:51 And W3, the triple? What is it based on?
**Steve Rao** 14:54 Yeah. Go ahead.
33 is triple. It's, extended, protocol based on GRPC. Yeah, maybe I think, yeah, if we… Yeah, if GRPC is HTTP tool here, maybe we can… I use similar strategy.
**Liudmila Molkova** 15:15 But then both W2 and triple would be HTTP…
**Steve Rao** 15:22 Probably.
**Liudmila Molkova** 15:23 2.
**Steve Rao** 15:24 Yeah.
**Liudmila Molkova** 15:27 It's like, if you're…
**Trask Stalnaker** 15:28 The question is how to differentiate.
**Liudmila Molkova** 15:30 Yeah, do we need to? And if we need to, then how?
**Steve Rao** 15:41 It's a different… yeah, maybe, yeah, it's a documentation, too.
**Liudmila Molkova** 15:49 So, I have a precedent for… JSON RPC, we have JSON RPC protocol version, because it's orthogonal.
I can explore it for a double protocol version.
**Steve Rao** 16:06 Hmm.
Yeah, this is, yeah, different between triple and, Grpc, yeah, it's… it's introduced a relationship with the gRPC protocol.
**Liudmila Molkova** 16:20 Oh, I remember we… we thought it was the idea of capturing the header.
But it's… Not… Where you go.
So, should we then, I think that there are two possible options where you introduce a new attribute, Or… Or we just don't differentiate.
**Steve Rao** 17:25 Hmm… Yeah, you, you mean, In here, maybe W2 is not a suitable value in network protocol name, and maybe we need to introduce a new attribute.
To record that value.
**Liudmila Molkova** 17:46 Let's see… Oh, okay, so, okay, so the W2 is TCP only, it's not based on HTTP.
**Steve Rao** 17:55 Yeah.
**Liudmila Molkova** 17:56 Oh, I see, okay. Now, that, that, that… So let's see… Networked Protocol Name.
Is double 2… Versh… version is whatever?
Transport is… GCP?
And for double 3, for triple, it's HTTP version is 2, and transferred is TCP.
Should they… or different.
**Steve Rao** 18:37 Yeah.
**Liudmila Molkova** 18:46 Probably you don't even… care about version here? I don't know.
**Steve Rao** 18:53 Mmm, yeah, yeah, in W2, maybe…
**Trask Stalnaker** 18:56 Was there a double one?
**Steve Rao** 19:00 No.
**Trask Stalnaker** 19:00 protocol.
**Steve Rao** 19:02 No.
Yeah, we, yeah, double, yeah, when it's, open source, it's from W2.
Yeah, without a double one, yeah.
Being in open source.
**Trask Stalnaker** 19:23 Lyudmila, what do you think about putting the two on the version?
**Steve Rao** 19:29 Yeah, yeah, I think he's okay.
**Liudmila Molkova** 19:37 Okay, yeah.
**Steve Rao** 19:45 Cool, then we don't need new attribute.
**Liudmila Molkova** 19:48 We can… Highlighted in the… Where else?
**Steve Rao** 20:00 Yeah, in another option, yeah, maybe we can also delete the version 2 in W2.
Generally, yeah, people just know the double particle instead of a double tube.
Do we need to highlight the version 2 here?
Yeah, forgot about you?
**Trask Stalnaker** 20:22 Do we want to say that version has a default value of 2?
**Steve Rao** 20:28 Yeah, the default value, yeah, is W2.
There are just one protocol in W2.
That is the default protocol.
Do we need to highlight the… the other version here, or not?
**Trask Stalnaker** 20:56 What do we do, for, like, gRPC for HTTP version 2?
**Liudmila Molkova** 21:27 Nothing. I just always said it.
**Trask Stalnaker** 21:30 Yeah.
**Liudmila Molkova** 21:32 But it actually… Not great, because it's… Always would be 2 for gRPC, like, almost always.
Okay, at least it's not tied to… Largely follows.
**Trask Stalnaker** 22:33 And I don't know if… I mean, would unary cause… I mean, in theory, unary calls could be over HTTP1, Unless they require… Trailers, even then, or something weird.
**Liudmila Molkova** 23:08 Well, at least, Gemini thinks it's not.
And this is dark night.
I mean, maybe, but, but…
**Trask Stalnaker** 23:37 Yeah, yeah, not in practice, okay.
**Liudmila Molkova** 23:43 And… We can.
Believe the attribute, we can just say The default is 2 for gRPC.
**Trask Stalnaker** 23:56 Well, that service… Long-term, like, if it's done 3 later…
**Liudmila Molkova** 24:07 Then we will have defaults that But I'll need to change in perspective of 10 years.
Not the end of the world we can handle it at some point.
**Trask Stalnaker** 24:28 What about transport?
Hmm…
**Liudmila Molkova** 25:16 So, it sounds like it can, in theory, run over UDP and HTTP servers.
Just somehow, somebody implement.
**Trask Stalnaker** 25:39 Okay, but it's not.
Like you said, though, it's not… So maybe we could consider defaults. Now, do you… One of the questions with defaults, we were generally only applying defaults.
When it wouldn't be confused with unknown, Do we…
**Liudmila Molkova** 26:07 Right.
I don't… You cannot distinguish unknown from the default.
Is it a problem here?
**Trask Stalnaker** 26:45 Here's what we did for HTTP, did we… At least, say, the default.
Network protocol name conditionally required… If not HTTP, okay.
So that's… Reasonable.
**Liudmila Molkova** 27:15 Oh… We're actually…
**Steve Rao** 27:18 That's a little default.
**Liudmila Molkova** 27:21 Sorry, go ahead, Steve.
**Steve Rao** 27:23 Yeah, no problem. Yeah, I just see the trans network transport, yeah.
**Liudmila Molkova** 27:30 The transport is even obtained, because we at some point thought, Who even… Airs.
**Trask Stalnaker** 27:38 Mmm… I like that.
**Liudmila Molkova** 27:43 Yeah.
protocol version… Vertical name… 7, if not a shitty GP, yeah.
Yeah.
So then, what we can do for GRPC… Networks.
Protocol name… So it's…
**Steve Rao** 28:29 It should be…
**Liudmila Molkova** 28:29 HTTP is default.
**Trask Stalnaker** 28:34 So, conditionally required, if not HTTP.
**Liudmila Molkova** 28:38 Yeah.
The network… Radical version… If not 2… Network… transport…
**Trask Stalnaker** 29:02 Optin.
**Liudmila Molkova** 29:07 Okay.
Where would it leave us?
with… So we have network peer address and peer… Word.
**Steve Rao** 29:24 Yeah.
**Liudmila Molkova** 29:25 We also have them for HTTP period.
Yeah, recommended.
Okay.
And then, in most cases, then, we wouldn't have this friends, which is actually good.
Yeah.
And it was Shajit for everybody, then.
**Trask Stalnaker** 29:58 Well, we should do it for… Dubbo.
**Liudmila Molkova** 30:01 I see, but… okay, so we can do it for everybody.
But everybody would have different defaults.
**Trask Stalnaker** 30:09 Yeah.
**Liudmila Molkova** 30:10 Yeah.
And, like, connector pieces…
**Trask Stalnaker** 30:14 Except maybe JSON or PC.
**Liudmila Molkova** 30:18 JasonRPC, it's just transport agnostic.
Right. Maybe if we should just remove all the stuff from it, because… Makes sense.
**Trask Stalnaker** 30:28 Hmm…
**Liudmila Molkova** 30:28 We're… Either remove it at all, Or… Never have any defaults, because there are no defaults.
Oh.
We are not stabilizing JSON RPC, though.
**Trask Stalnaker** 30:43 No. No.
I don't think so.
I think just gRPC and Dubbo.
**Liudmila Molkova** 30:54 Yeah, and, like, the connector PC would… and DABO, since they support HTTP11 clients.
They might have HTTP11.
tributes.
Which is… which is fine, because it's the same default, if not HTTP2.
Okay.
And so, for double, it also becomes opt-in, right?
**Steve Rao** 31:34 Yeah.
**Liudmila Molkova** 31:39 This becomes… If not 2, right?
This also becomes if not too.
Even though it's different, too.
**Steve Rao** 32:00 Yeah, yeah, yeah, in here, yeah, I'm just, yeah, we have the same version in WG and double C, that is to make users confused, so at least, yeah, maybe, yeah, we can consider delete, delete, delete the… Version 2 in Papua 2.
**Trask Stalnaker** 32:21 Do we care about any of them?
Well, I was looking at database, and we didn't include… I mean, so the network… Protocol and network transport are all opt-in over there.
I'm wondering if… We should just do the same for RBC.
**Steve Rao** 32:46 Okay.
Okay.
**Liudmila Molkova** 32:58 Thinking… So they should not show up on metrics, anyway.
Well… Maybe versions could.
Do they include them in metrics?
**Trask Stalnaker** 33:12 I mean, they're low cardinality, so I think we… Good.
**Liudmila Molkova** 33:20 Yeah, but you could, but do we want to?
**Trask Stalnaker** 33:26 If we don't want them on metrics, then I would… Question, having them on.
span… I mean…
**Liudmila Molkova** 33:36 We can, we can make them up tin?
But it's pretty much equivalent to not adding them and letting somebody come with the feedback that they are necessary. You can always set them as opt-in later.
**Trask Stalnaker** 33:53 Oh, yeah, I guess I… to me, that's the same thing.
Of removing them.
To be clear, on database, on database, they're not present.
list.
Yeah.
And I'm kinda leaning that direction for RPC.
**Liudmila Molkova** 34:29 So, I think I have an argument in this favor.
No, we have them. Oh, the… the… the address and port. Oh, I see.
I see.
So then… We can remove this reference from the generic.
conventions?
The individual ones can keep them if they want to.
We would probably remove them.
From gRPC.
Steve, if you want to keep the double, the network critical name, I think it should be fine.
**Steve Rao** 35:32 Okay.
**Liudmila Molkova** 35:37 R… And we'll remove them from the connector PC, I guess.
Well, I can't… if I… I don't know, but if I hosted ConnectRPC server, I would know if people are connecting using HTTP1 or HTTP2.
Like, your PC or HTTP.
Or maybe I would rather enabled the… The metadata to say, or the… HTTP headers to say, to identify the content type.
**Steve Rao** 36:27 Okay, yeah, yeah, I'm… yeah, I'm taught that, I'm… I need to… yeah, add the metadata to double or not, yeah. In double, it also has similar, concept called, attach.
**Liudmila Molkova** 36:45 Oh.
**Steve Rao** 36:46 Yeah.
**Liudmila Molkova** 36:48 Are you…
**Steve Rao** 36:50 Yeah, I don't contend it here.
**Liudmila Molkova** 36:52 Okay.
**Steve Rao** 36:53 But, yeah, I'm told that, whether I need to contain them in our double semantic convention.
Yeah, the, attachment, it can be used to have user to transport some, key value.
Prevalue that, yeah, in double.
I think that it's a similar… concept with, metadata from gRPC or other GRPC protocol.
**Liudmila Molkova** 37:29 Yeah, and you can add it to your PR, but you don't have to, like, you can follow up.
**Steve Rao** 37:34 Okay, yeah. Yeah, I can add them later, and maybe we can discard them later if they are any problem.
**Trask Stalnaker** 37:49 Let's take CONDAC.
our PC, like, do… Do you know, assuming you're… Does Conne- would ConnectRPC Instrumentation know if it was using 11 or 2.0?
I guess it depends on the… like, when thinking of if it was built on top of, like.
I'm HTTP.
Library or something.
**Liudmila Molkova** 38:27 Good question.
I mean, the… we can dig it up.
But I would rather dig it up for gRPC, would we know for gRPC?
Okay.
**Trask Stalnaker** 39:00 Yeah… I would think, like, And the… I would think, like, gRPC native instrumentation could?
But not sure… about… the instrumentation that we write on top of gRPC, if it would… I mean, there's likely… Some way to get access to that.
**Liudmila Molkova** 39:51 And I can take a look at this and investigate, maybe there are some other characteristics that are more useful than HTTP version.
That are available.
Okay, we are almost to…
**Trask Stalnaker** 40:12 I do agree with you, though, that, Like, it is… an interesting, like… It is a potentially interesting dimension.
to know if, like, it… at least, like, for the Kinect.
Or… Dubo, which support both 1.1 and 2.0.
**Liudmila Molkova** 40:42 I feel like that.
**Trask Stalnaker** 40:45 Right.
**Liudmila Molkova** 40:46 Steve, do you know if you can, like, access the HTTP version?
From the instrumentation code.
**Steve Rao** 40:56 Okay.
You, you mean, so, from, from Java instrumentation code?
**Liudmila Molkova** 41:05 Yeah, like, if you're instrumenting the… DABO Server.
And some people would use gRPC client, some people would use HTTP client.
Could you know on the server side which one was used? Like, especially in the instrumentation?
**Steve Rao** 41:27 Mmm… Sorry?
**Liudmila Molkova** 41:35 Yeah, can you repeat it again?
Yeah, of course. So let's say, I'm, I use HTTP client, and it talks to my, double, my triple server.
And I also have another client, which is your PC client.
It also talks to the same triple server.
**Steve Rao** 42:00 Hmm.
**Liudmila Molkova** 42:00 it's useful for me to know, like, if somebody came through HTTP or through gRPC, right?
**Steve Rao** 42:09 Yeah.
**Liudmila Molkova** 42:13 And… what would be, like, the way… like, do you know in the triple server?
Like, do you have the API that can tell it, or how would… Instrumentation, no.
**Steve Rao** 42:28 Yeah, maybe I can do some research at this point, but I think, yeah, in protocol, there is protocol information, maybe we can get… To distinguish the different, clients.
Yeah.
Yeah, I can do some research at this point, for this point.
**Liudmila Molkova** 42:51 Okay.
Cool, let's… let's figure it out, and I can take a look at the Connect and see maybe gRPC.
Cool. Anything else we should talk about here? It sounds like… Steve, you will update it to… Document differences, right, between versions.
**Steve Rao** 43:22 Yeah.
Yeah, I can update them later, and maybe we can have another review later.
**Liudmila Molkova** 43:30 Yeah, of course. Thank you.
**Steve Rao** 43:32 And no problems.
**Liudmila Molkova** 43:35 Yeah, we don't have time.
**Trask Stalnaker** 43:37 on the target.
**Liudmila Molkova** 43:39 Yeah, let's quickly talk about the target.
So… I have examples here which are… and it should also apply to you, Steve, with, was double.
So there are quite a few… ways… one can provide a gRPC URL, right? So it could be this.
It could be this… And this, these two are fine.
This is the server address, this is server port.
**Steve Rao** 44:20 Okay.
**Liudmila Molkova** 44:22 But let's say we have load balancing with Zookeeper.
This is the zookeeper address.
It's not, it, it's, it's like the, the, the, the… The main resolution server, yeah.
But I initially, thought that, okay, let's just drop it.
But I played with Java instrumentation for gRPC and gRPC, And for things like this, it considers this to be the authority in our instrumentations currently.
Populates… this.
Which is not a terrible fallback. It's not awesome, but it's not terrible either.
So yeah, that's the proposal here. And.
**Trask Stalnaker** 45:21 Oh, you updated. Okay, I saw your comment earlier, but I didn't see your update.
**Liudmila Molkova** 45:27 Yeah. I think it's fine.
I would appreciate you reading through, because you have a great eye for the unnecessary complications, and if you feel like anything can be simplified, we and ChatGPT spent enough time on this, we… we are, My mind is…
**Trask Stalnaker** 45:48 The Zookeeper is… You confirmed that's what the gRPC native instrumentation captures?
Or you're saying that's what OpenTelemetry Java instrumentation captures?
**Liudmila Molkova** 46:03 So the native captures target URL, it captures this thing, whatever it is.
**Trask Stalnaker** 46:10 Oh, yeah.
Oh, right, it has that separate field for the target, yes.
**Liudmila Molkova** 46:17 Right.
**Trask Stalnaker** 46:18 Do they not capture server.address?
**Liudmila Molkova** 46:23 Not… not separately.
**Trask Stalnaker** 46:24 Okay.
**Liudmila Molkova** 46:26 But they would also capture this, which is a list of IP addresses.
And I'm… I'm suggesting not to, because I… I don't know. I don't believe it's useful by any means.
**Trask Stalnaker** 46:40 Hmm…
**Steve Rao** 46:46 Okay, yeah, you, you mean, so maybe in, in, separate double, page, yeah, maybe we also need to, yeah, provide some similar example in, server.js server port?
**Liudmila Molkova** 47:00 And you also support this scenario when somebody provides the Zookeeper URL.
And it would return the list of actual IP addresses or endpoints. And if we pick… Like, if… I'm curious if it makes sense for you, and yes, if it does, it would be great to also document it.
**Steve Rao** 47:20 Okay.
**Trask Stalnaker** 47:25 So the alternative here to this PR would be… Capturing the target… having gRPC.target.
Is that what they call it?
**Liudmila Molkova** 47:39 And… yes, the, that, that JRPC, that target, yeah.
**Trask Stalnaker** 47:44 We could capture gRPC.target and accept that there's some duplication.
**Liudmila Molkova** 47:54 Or, when we cannot reliably parse the three guys captured your PC target.
Conditionally required, or say it's opt-in.
**Trask Stalnaker** 48:07 Sorry, I didn't follow.
**Liudmila Molkova** 48:10 It's like, we can… you can say, okay, if… if you cannot parse server address port.
Then populate your PC target.
**Trask Stalnaker** 48:19 Oh, to avoid the duplication.
**Liudmila Molkova** 48:22 You can do.
**Trask Stalnaker** 48:22 national.
**Liudmila Molkova** 48:24 Yeah.
**Steve Rao** 48:28 I have a small question here. You mean if we don't, get the server address server port, yeah, maybe we can, we can set a, server, server string, like here, the last one, yeah. There are two… IP… IPv4 address.
**Liudmila Molkova** 48:55 So if it's one APB4 address, it's fine, but if there are multiple, Hmm. I have a problem.
And… We… Need someplace to… Recorded.
And we would use gRPC-specific. For gRPC, Kafka might have something similar, like the bootstrap servers.
But it would be Kafka-specific, then.
And so on.
**Steve Rao** 49:30 Okay, yeah, maybe we can… I can, yeah, read the PR specifically, and yeah, maybe if I have any question, I can leave the comment later.
Yeah, I see.
**Liudmila Molkova** 49:40 Yeah!
I'm not sure, I didn't check, I probably should… if… if double supports, something that when you get a list of IP addresses, it would be great to know.
**Steve Rao** 49:53 Yeah, you… okay, yeah.
**Liudmila Molkova** 49:59 Okay, let's take another look at this one.
Oh, sorry.
Cool.
Great discussions.
**Trask Stalnaker** 50:27 Right, yeah.
Good to see you both.
**Liudmila Molkova** 50:31 Anne, good to see you.
**Trask Stalnaker** 50:33 Bye.
**Liudmila Molkova** 50:34 Good rest of your week.
