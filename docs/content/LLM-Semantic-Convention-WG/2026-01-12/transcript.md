SIG: LLM Semantic Convention WG
Date: 2026-01-12
Duration: 15 minutes
============================================================

## Zoom Recording Transcript

**Keith Decker** 01:47 Morning, yes.
Give it a few more minutes here, see if anyone outside our team shows up.
**aditya (cisco/splunk)** 04:16 Hey, hello, good morning, guys.
**Ridhima Satam** 04:19 Hey there.
**aditya (cisco/splunk)** 04:22 I can… I'm just catching up on the thread.
Sergey, Tangbil.
So, yeah.
There is this new semantic conventions PR that… Nakumar from Microsoft has opened a PR.
to that.
That is something that I can… Go over quickly.
If everybody… wants that.
But, you know…
**Ridhima Satam** 05:08 Can you add that to the agenda?
Adapto.
That'll be our link, and…
**aditya (cisco/splunk)** 05:15 Agenda, you mean?
Meeting notes.
**Ridhima Satam** 05:20 Yeah, the meeting notes agenda.
**aditya (cisco/splunk)** 05:23 That's a Google Doc, right?
**Ridhima Satam** 05:27 Yep.
Do we have the link?
**aditya (cisco/splunk)** 05:30 Yo.
**Ridhima Satam** 05:31 Cement.
**aditya (cisco/splunk)** 05:32 I'm an insurance.
**Ridhima Satam** 05:35 Yeah.
**aditya (cisco/splunk)** 05:38 Why is it still working?
But that's an OpenTelemetry LLM semantic convention link.
the demo.
**Ridhima Satam** 05:57 Oh, so is it not… this is not the open telemetry NM? Semantic conventions?
**Keith Decker** 06:03 The meeting notes have been for both this meeting and the semantic conventions, so you'll see both of them in there.
**Ridhima Satam** 06:11 Yeah, I mean, you are talking about agents, right? Yeah, we are making same notes, so if you go to that link I just shared with you, Aditya.
**aditya (cisco/splunk)** 06:22 Okay, so you've been, like, I should create an event record?
Okay, you said AI agents track, right, okay.
content.
The original PR is from… don't have much to add to it. It is just that we have a… team in Cisco, which is called AI.
Defense team, which are creating something similar to… Do other… are other people also dedicated to the students, or is it just me?
**Ridhima Satam** 06:58 We are good.
**aditya (cisco/splunk)** 07:02 Okay.
virtue.
Jet, check.
Okay, I think I'm good now, too.
So yeah, so they have something similar to guardrails.
For that, I have created a… SDK.
In a… in the same, like, an instrumentation SDK?
So that is something that we have to… Earlier, the plan was not to have it in the upstream repo, but I think things will change.
If one's this fiatis.
Accepted.
Hell yeah.
I'm just looking up for that PR.
**Ridhima Satam** 07:51 So, one more thing here, like, so this meeting is just for the AI agent. I did not attend previous meetings.
I think. Oh, I don't have the context exactly. I will just go on to discuss agentic, related.
It's my understanding, like, looking at the title, it's just the agentic workflows, or…
**Keith Decker** 08:14 Yeah, this meeting is meant for AI agent stuff, but as with any of the OpenTel, you know, other areas kind of spill into it if you have people on that.
you know, work in those… those other areas. But, yeah, this one is specifically for agents.
**aditya (cisco/splunk)** 08:32 Yeah, that was my understanding, too, and I don't know what Sergei means today's meeting, just to provide support or meeting notes of any problems.
I don't know, Kamara, maybe you can provide an update on… No, of course. Because this guardrail… PR, right.
It's totally something not related to the jets.
**Keith Decker** 08:56 Aditya, go add that PR to the agenda here on this document.
So, it's in the notes of… Things that were talked about.
**aditya (cisco/splunk)** 09:05 No.
Yeah, yeah, but… I can add it, but not sure if it is related to AI agents track.
Right? So, that's why. But I've added it anyways.
Because I don't know… do you guys know if Nakkumar has brought it up in any of the SIGs? I don't think that it has been discussed right yet.
By him.
**Keith Decker** 09:32 I don't think so.
**aditya (cisco/splunk)** 09:33 Yeah, so I don't know if I should re… Yep.
integrate it, but I've added it there.
I did leave some comments on the PR. Keith, something related to what you and I were discussing.
Like, having a new type in the GenAI utils.
For security-related stuff.
And that's what I've also… conveyed to Nakkumar that he can have… we can have a new type in Gen AI Utils.
Or the guardrails band that they are… Trying to introduce in the instrumentation.
I'll tag you in the comment as well, so that if you have anything, you can…
**Keith Decker** 10:21 Okay, yeah, I can go work about.
**aditya (cisco/splunk)** 10:24 Yeah.
But I think it would be good to have that new type.
For security-related spans.
**Keith Decker** 10:52 For yours, Redeema, did… Do you have anything you want to talk about with this group? I know this is all our team, so do you want to… Do anything here, or wait to see if we can get…
**Ridhima Satam** 11:06 Outside team conversation.
Are you talking about the workflow PR?
**Keith Decker** 11:11 Yeah.
**Ridhima Satam** 11:12 Okay, let me share my screen.
Okay, yeah, so basically, I actually thought that it could be tomorrow, so it's still in draft. I can move it so that maybe if there are any errors, we're just waiting for any In Vietnam.
reviews for that, so… For this proposal, we had this proposal earlier to have a workflow separate span, but during the discussions, I think it came out that we have… we can add the workflow as operation name in the agent span instead, so… that's what I've done here. It's mostly just changing the operation name, so… Not changing, adding one more operation name. So if you go in here.
This is the current agent spans, and we have create agent span and invoke agent span, then we will have the invoke workflow as an operation name. So, this operation name could be in workflow.
And the name of the workflow.
So, I have added those changes in there, and yeah, most of the files, if you see, they are, like, repetitive in many places you have to add that invoke workflow, say, in AWS Pedrock, where you are giving them examples of… so, it's mostly repetitive. I just looked at, I think, Josh's ER and compared the files there. So, maybe, Josh, if you can take a look, I think you have the retrieval span PR… I mean, operation name changes, so… Yeah, I made similar changes most places, so just take a look, like, if I missed anything otherwise.
So, otherwise, the changes are very… Saying, like, I have added this GenAI framework, one more attribute.
Let's see, tomorrow if we have 16.
If they have any comments about it, but otherwise, yeah.
That's all it has.
Pam.
That's it.
**Keith Decker** 13:38 Thank you.
Yeah, and get somebody to look at that, and then bring it up tomorrow.
**aditya (cisco/splunk)** 13:46 Also, do these sick PRs have a… Like, chain set size? Like, how many lines of code is required?
Because Nakkumar's PR is, like, 14,000 lines of code.
So I'm not sure… SIG is okay with that many lines of… changes in a single PR.
**Keith Decker** 14:08 They generally are not, so I imagine that one's gonna… Get a lot of pushback.
**aditya (cisco/splunk)** 14:14 With that travel.
**Keith Decker** 14:14 I like to keep things at about 500 lines or less. I've seen some bigger ones sneak through, but a lot of those are boilerplate-y ones when they're bigger.
**aditya (cisco/splunk)** 14:24 Yeah, this PR introduces a lot of things in a single chain.
And even I had to, like, Thursday and Friday, I went over it, and it was a lot of code.
For me to go over.
He was, okay.
**Keith Decker** 14:52 Alright, anything else on our agenda?
Doesn't look like it. Anything else to discuss?
**aditya (cisco/splunk)** 15:02 From my side, because I'm also waiting for the AI defense team to get back on a few things.
And I have tagged them as well.
Because a lot of things are being introduced in this PR, so it's better that the domain team also takes a look at What attributes that are needed?
Exactly.
For their use cases.
But yeah, that's all from my side.
**Keith Decker** 15:33 Hmm.
Well, thanks all. I guess we'll get some time back today.
**aditya (cisco/splunk)** 15:39 Okay, cool. Thank you, guys.
**shuwpan** 15:42 ill.
**Ridhima Satam** 15:43 Thank you, bye.
