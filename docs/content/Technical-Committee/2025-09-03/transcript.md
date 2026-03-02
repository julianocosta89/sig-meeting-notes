SIG: Technical Committee
Date: 2025-09-03
Duration: 9 minutes
Zoom Recording URL: https://zoom.us/rec/share/NO2D8S8VdCF8_43rWoWJd-TLsYcwzWE7I7c_E72hnBEkmzTGsceMwrTPXR_4rr5t.CLmQOxzSNLf6hHJF
============================================================

## Zoom Recording Transcript

**Tigran Najaryan** 00:40 Hey, Riley, how are you?
**Reiley Yang** 00:44 Good morning, Taylor.
**Tigran Najaryan** 00:46 Morning.
**Reiley Yang** 00:47 Well, how are you?
**Tigran Najaryan** 00:50 I'm good.
**Reiley Yang** 00:59 It falls.
Couple minutes.
Meanwhile, we can look at the spec triage.
Let me share my screen.
Can you see my screen?
**Tigran Najaryan** 01:17 Yes.
**Reiley Yang** 01:25 Okay, so there's…
**Tigran Najaryan** 01:27 I like emptying boxes.
Nice.
**Reiley Yang** 01:45 I also have a question here, I want to know your feedback, so…
We don't do this anymore. Do you think we should keep it or remove it?
**Tigran Najaryan** 01:57 Yeah, I don't think we need to keep it. The GC does the triaging, right? They move it.
**Reiley Yang** 02:02 Yeah.
**Tigran Najaryan** 02:02 TC inbox when there is a need.
I don't know why we would want to have it here.
**Reiley Yang** 02:12 Okay,
**Tigran Najaryan** 02:13 The… the main… the main backlog project port, what… what does that show? Can you open that?
Yeah, we use… Is it useful?
**Reiley Yang** 02:22 we used to track, like, major SPAC investments, but now we spread it across 6, and we don't do it centrally.
**Tigran Najaryan** 02:33 Yeah.
Yeah, I don't think we need to do anything about this. This is… Yeah.
**Reiley Yang** 02:49 Hey, Carlos, Josh.
Good morning.
**Carlos Alberto Cortez** 02:52 Hey.
**Tigran Najaryan** 02:52 Hey, guys.
**Reiley Yang** 02:53 We just, looked at the TC inbox, and it's empty, and I was asking Tigran, but I also want to get your feedback, so…
These items, we don't do that anymore, so do you think we should…
redirect that, or we should just get rid of that from the list. I also noticed the same thing from the spec sig. We mentioned we need to give people a time box for a certain topic, but we don't do it anymore, because that…
that person, or that sick doesn't exist anymore, so I want to make sure we have sanity here.
I would suggest that I simply remove both of them.
**Josh Suereth** 03:32 I think that's… that's fair. The,
We have a community inbox a second, yeah, I think that's fair. The only thing I might add, which I… you saw I'm starting to try to do last week, is…
proto.
Like, let's remove those two, and let's just do a check proto repo.
I don't expect it to have anything relatively, because, what, we get one issue a month or something.
Maybe.
But, just to make sure, we're regularly checking up the Pro.
**Reiley Yang** 04:02 Yeah.
**Tigran Najaryan** 04:07 Which reminds me, I think I promised you to take a look at the proto-issues last time, and I failed to do that, sorry.
**Josh Suereth** 04:15 It's fine, I was gonna ping you off… I… I, I took a long weekend, so after…
I think we had our meeting Wednesday, Thursday I had all-day meetings, and then I just was gone Friday. So, I didn't do anything useful since then.
So, my plan was to ping you, Tigran, like, just, let's take… I'll take an issue that I think is easy for us to resolve, let's talk about it in chat, make a PR.
**Tigran Najaryan** 04:39 Yeah.
**Josh Suereth** 04:39 Because there's a lot of low-hanging fruit to get rid of.
**Tigran Najaryan** 04:42 Okay, soundproofed.
**Reiley Yang** 04:56 Okay, so I'll just paste them here in case, like, we regret, we can come back later.
And I noticed the spec, spec doc has a similar thing when I was driving it yesterday, so I'll do the cleanup and mention it here. If we want to change anything, we can come back.
Okay, so… I want to see if we have other topics.
**Josh Suereth** 05:22 I have one public and one private. Sorry, let me add them. I'm waiting for docs to load. The public one, you can add… I think we need to regenerate the next set of rotations. So if you open up the rotation spreadsheet.
I think we're… we have one week left before we run out, and so I just wanted to ask, do you mind opening the,
Rotation spreadsheet?
It was still loading for me for some reason.
**Reiley Yang** 05:52 By the way.
**Tigran Najaryan** 05:53 And there's a lot of noise from your microphone, can you maybe switch to something else?
**Josh Suereth** 05:58 Oh, from mine.
**Tigran Najaryan** 06:00 I think it's yours.
**Josh Suereth** 06:01 Yeah, we have…
Is that better?
**Tigran Najaryan** 06:11 Yes.
**Josh Suereth** 06:12 Okay.
**Reiley Yang** 06:18 So now we just align the name. I don't think we need to…
randomly generate anything anymore, so we can start…
**Josh Suereth** 06:27 That's what I was gonna suggest, yeah, should we just copy from the top down?
**Reiley Yang** 06:32 Yeah. So we should just copy it from here, and let's see who's amazing.
**Carlos Alberto Cortez** 06:39 Jack.
**Reiley Yang** 06:41 Yeah, so I would put Jack later, like, I…
**Josh Suereth** 06:47 I think it's… when does he get back? Dude, I'm trying to remember.
**Tigran Najaryan** 06:51 I saw a comment from him today.
**Reiley Yang** 06:54 Yeah, same here.
**Tigran Najaryan** 06:58 Maybe he's back, I don't know.
**Reiley Yang** 07:00 Let's just put Jack here.
If that's fair.
**Carlos Alberto Cortez** 07:06 But to be honest, I think that sometimes he comes and checks something, provides feedback, and then he disappears, so we should just, instead, just ask him directly, you know?
**Tigran Najaryan** 07:14 Yeah, if he's not back by then, then we can, I guess, move him, bump him down further the schedule.
**Reiley Yang** 07:20 I asked him, even for the TC member, like, the new TC member recruiting, I asked him about his feedback. He responded immediately, and he's saying, although he's on vacation, but he's still online, but I don't want to…
make it an official job for him, so I… I would just, like, copy the existing list and add Jack in the end.
**Carlos Alberto Cortez** 07:46 Yeah, I think we could just, like, one week before death, if he's not back, just grab him or ping him, and yeah, but just jump.
**Reiley Yang** 07:54 So let's stick with this plan, at least for now.
**Tigran Najaryan** 07:59 Okay.
**Reiley Yang** 08:21 Okay.
Anything else before we switch to the private room?
**Josh Suereth** 08:27 I'll ask a quick question, how many folks are going to KubeCon in NA?
That one?
**Armin (Dynatrace)** 08:36 Not me.
**Josh Suereth** 08:38 I will be there, mostly because I got lucky with our, you know, travel approval lottery.
If you will.
Okay.
**Reiley Yang** 08:53 Okay, then we'll… we'll see everyone in the private room. Thank you.
