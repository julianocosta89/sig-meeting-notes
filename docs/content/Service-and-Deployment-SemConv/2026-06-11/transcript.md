SIG: Service and Deployment SemConv
Date: 2026-06-11
Duration: 41 minutes
============================================================

## Zoom Recording Transcript

**Yoshi Yamaguchi** 01:36 Hi, Aish.
**Ayushi Asthana** 01:39 Hello?
**Yoshi Yamaguchi** 01:42 How are you?
Are you talking now?
Are you talking now, Aish?
**Ayushi Asthana** 02:50 Mauna and Yoshi.
**Yoshi Yamaguchi** 02:53 How can I hear you?
**Ayushi Asthana** 02:57 I'm having some bandwidth issues today.
**Yoshi Yamaguchi** 03:00 Oh, I see.
I assume that today's topic is only about the service owner attribute.
Is this correct?
**Ayushi Asthana** 03:11 Yeah, I think, I think that is the only open item for discussion. For the rest of the things, we have some PRs and review.
there is also a few open items on the data attribute. We could probably discuss them.
Like, once we have… Gone over the owner attribute problem.
Let me add the meeting notes.
Let me share my screen now.
I'll present the meeting notes.
I think last time around, we didn't have anybody attending in the, evening time slot, so it was just me and Urjita. We didn't… disclaim.
**Yoshi Yamaguchi** 04:09 Yeah, I saw, I saw, yeah, I saw the message from Josh.
Last week.
**Ayushi Asthana** 04:13 Yeah.
**Yoshi Yamaguchi** 04:14 Yeah, yeah.
**Ayushi Asthana** 04:15 Yeah, so there was, like, nobody we were on the call for, like, 5 to 10 minutes.
But that's cool. So, I think the proposal for owner was out. I saw you had a comment here.
**Yoshi Yamaguchi** 04:29 Yeah, I made a comment last… two weeks ago.
About… The service owner attribute.
And then still, we don't have the, A common conclusion for the attribute, but overall, we are really positive.
for… to introduce this attribute, so… once… I'm not sure, like, other… because I couldn't… I couldn't… Aggregate their opinions on… This attribute from the multiple The product team internally.
But the overall, the direction of introducing this attribute is really positive.
So, I assumed that.
**Ayushi Asthana** 05:17 Okay.
**Yoshi Yamaguchi** 05:18 Once this is introduced into the standard, then…
**Ayushi Asthana** 05:22 I mean.
**Yoshi Yamaguchi** 05:23 the standard convention, then… The product team in… our product team will, like, align with the…
**Ayushi Asthana** 05:32 Yes.
**Yoshi Yamaguchi** 05:32 With this, this label.
**Ayushi Asthana** 05:36 Okay. Stop.
Love it.
I… I wrote it in the notes, in fact, that is… better.
Got it. So I think then we can start drafting a PR, and getting approvals on the PR.
Somehow observed that it's taking more time now?
But I think we just need to follow up a little more closely.
Yeah, so another… so we have, like, a couple of PRs currently open. One was for criticality attribute.
That we would want to move into alpha now.
So I had…
**Yoshi Yamaguchi** 06:35 I didn't realize that… that one… I didn't realize that one is still open.
for…
**Ayushi Asthana** 06:41 Yeah, kind of going for stabilizing it. I want, like, we were proposing stabilizing it, but we are unable to get the necessary buy-in to stabilize right now.
**Yoshi Yamaguchi** 06:56 See?
**Ayushi Asthana** 06:56 So, it was proposed that you can, you know, if you want to move the, sort of, life cycle forward, we could move it to Alpha and get more feedback from folks who are listening to, attributes that are in alpha and hotel. I see. So… This was one of the other things that we are working on, marking service.criticality in alpha. Right now, it's in development.
So, if you could get more feedback or more positive responses on the use cases in criticality, we could potentially move for stabilizing it as well.
So, that is… that was the intent. I'd earlier opened the PR for stabilizing it.
**Yoshi Yamaguchi** 07:46 So I'd like… I'd like to… I'd like to learn how the Google team is utilizing this Label this attribute into, for, for… your services, like… Cloud… Monitoring or cloud traces?
So do you, like, do you… So, yeah, are they, are they using this label for the annotation?
Of, like, special cases, like, for example, if, like, highlighting the specific service… The specific span from the… this… like, criticality, high services.
in, like, waterfall chart of the cloud trace, or, like, how do you actually use it?
**Ayushi Asthana** 08:35 So, I think you must have heard about the AppHub… service, right? A service that GCP… is starting, where we are, sort of allocating actual GCP resources, like computes and disks, to services and workloads within an application. So it's kind of an abstraction on actual infrastructure pieces and marking them as Either services or workloads that run within an application. So right now, the use case internally with GCP is marking specific services or workloads as critical.
Oh, yeah, so…
**Yoshi Yamaguchi** 09:17 So you're using… so the Google is internally using this label to… for… for the… to decide which service is more important than others.
And then, do you… do… do… does Google Cloud pro… any specific features for the users on the GCP services?
Using this label?
**Ayushi Asthana** 09:42 Yes.
Yeah, so that is… that is the idea going forward, that, services remarked critical. I think there are some features that exist within Apple at the moment. I would have to look it up, I think. I save it.
**Yoshi Yamaguchi** 10:01 I see. Then, I will bring… that use case is into the discussion internally, I mean, Grafana Labs internally, and then let's see how it goes. Maybe we can buy in.
the… the… the poor doctor team for… for stabilizing Standardizing… stabilizing… stabilizing?
stabilizing.
Stabilizing this label, yeah.
**Ayushi Asthana** 10:27 Right. I think, I think I can share AppHub documentation on criticality, what criticality is marked as. Currently, users can set criticality and environment on specific services.
Or on workloads.
And I think we're in the process of building features around it.
So that… things that are marked critical are treated differently in security domain or in observability domain within GCP.
**Yoshi Yamaguchi** 10:58 Yeah, that's really helpful. So I… it'll be… so it's… it's… so it… the document is shareable to others, right?
the AppHub.
use case. Yeah, that's really helpful.
**Ayushi Asthana** 11:10 Yes, it's a publicly available feature as well.
**Yoshi Yamaguchi** 11:13 I see.
**Ayushi Asthana** 11:18 I'll probably take an action item to add documentation for… Well, I'll add it over here in the notes, try to get this to you. I mean, I'm… I was just… Just looking at documentation, but it's not easy to find stuff on the call, so I'll do that.
**Yoshi Yamaguchi** 12:05 Yeah.
One question, so do you have any deadlines?
for… to, to, to… to make this, like, to make the, criticality label, stable.
And also, do you have any criteria to… to get the…
**Ayushi Asthana** 12:23 Yeah. Nice.
**Yoshi Yamaguchi** 12:24 Like, criteria for… for the approval, I mean… Such as the number of the companies to, like, agree upon, or, like, I'd like to know… Such kind of data.
**Ayushi Asthana** 12:41 Yeah, I think I'd confirm that with the Josh, if there is, like, a strong criteria that exists. I don't think there is one right now. So, last we talked, it was mostly just, you know, if you get enough plus ones, and people agree, you can go ahead and stabilize it.
So I don't think that…
**Yoshi Yamaguchi** 13:01 Yes.
**Ayushi Asthana** 13:01 Strong documented criteria that exist.
**Yoshi Yamaguchi** 13:03 Yeah, at least I can put plus one to, to, to this.
this suggestion.
**Ayushi Asthana** 13:10 Yep.
**Yoshi Yamaguchi** 13:10 That's… that's… Come on!
**Ayushi Asthana** 13:12 What is the proposal for stabilizing?
**Yoshi Yamaguchi** 13:14 It does sum up?
works.
On… I mean, putting the plus one onto the… yeah, this one. Yeah, I did.
I did it, I put it.
Yeah.
**Ayushi Asthana** 13:29 This is the proposal for stabilization.
So, we're moving to alpha, but we'd like to close off on stabilizing probably by, like, July or August. I mean, the sooner we can get it done is the better, but… We're tracking July or August to get it stable.
And whatever we can do to expedite it.
**Yoshi Yamaguchi** 13:52 Nice. Okay.
**Ayushi Asthana** 13:56 So this is for, criticality.
Then the… Other thing that's open right now within the SIC is data attribute groups.
So… I think… is there anything more for us to discuss on criticality?
**Yoshi Yamaguchi** 14:17 I see.
Okay. And then, so, if you need more, faster.
like, discussion, then could you raise the topic on the Slack channel?
The sequel…
**Ayushi Asthana** 14:32 She was like.
**Yoshi Yamaguchi** 14:32 Yeah, so we can, we can discuss the, discuss further on the Slack asynchronously.
**Ayushi Asthana** 14:41 Makes sense, makes sense. Yeah.
I'll start a thread on Slack on what it would take for stagnation.
**Yoshi Yamaguchi** 14:50 Yeah, any kind of… any kind of topics we… I'm happy to jump into.
Because… because I… I have, sometimes I have a business trip to other countries, and I cannot make… this… Regular meeting.
So… Now, I don't want to, like, ruin your time.
Because of that. So, I'd like to, like, you know, make more conversation over a synchronous way.
**Ayushi Asthana** 15:24 Right, that's fair. I think, I think I'll keep that in mind, move, like, more and more conversations to async, so that we close faster.
**Yoshi Yamaguchi** 15:33 Yeah, yeah.
**Ayushi Asthana** 15:33 be useful for us as well.
**Yoshi Yamaguchi** 15:35 Yeah, yeah.
Thank you.
**Ayushi Asthana** 15:37 Okay, so the… I think the last thing that I… we… I kind of had on my mind was for the data attribute.
group.
I… I'm not sure if you've seen the conversation for the working group that we had.
But basically, on this specific proposal, we got a lot of feedback from the working group about this attribute group being too broad for observability.
And, I've attached demos. I don't think we have formally discussed it in this APAC meeting.
But basically what we had proposed with the data attribute group was, basically something like… Sensitivity and category.
Attribute groups, which can be attached to payloads that can be attached to spans or services, and they will be treated differently during collection or storage or auditing.
So, I had also added demos for this. For example, this was one of the demos that had Wait, was I sharing? I was sharing, and then I stopped sharing.
**Yoshi Yamaguchi** 16:57 Yeah, it'd be great if you have a recording of the demo, or you can do a live demo now.
**Ayushi Asthana** 17:04 Yeah, yeah, we can… I can… we can probably… I don't think I can do a live demo, I'd have to bring up… but there are PRs, in hotel demo already, so I had added a PR for log redaction, was one of the use cases. So, basically, this… this attribute Or attribute group can be attached to, specific… so here I had, I think, added it to payments.
Yeah, I added this attribute to payment service, data sensitivity high.
And then, during collection, I had set that if data sensitivity is high, I was redacting specific sections of the log, or I was redacting the log body.
So this was one of the use cases.
That I had added a demo for.
So, this is what it looks like.
In… in practice, if you open up… You know, logs from service. There would be logs that would be redacted.
From the payment service, because you have configured them as such in the collection.
And the other use case for category?
I think it was when we were dealing with… I think the enum is yet to be decided, so what the category enum is going to be like, and we don't have, like, a very good like, consolidated resource and what all of the categories could be, but PII or financial were a few of the categories, and you could map out what services are dealing with what type of data.
Based off of this data category.
So this is one of the use cases.
Hmm. Oh.
D… So, people were aligned that the use cases are valid and we need something like this, but there were a lot… there was a lot of debate on the nomenclature for this. Like, do we want data as an attribute group, or is there something else possible that would be better?
or… is data going to be too broad? And then we will sort of… this will sort of blow up.
Out of proportions, and we would not be able to handle the volume of requests.
that come up for data as an attribute group altogether. So those are main concerns. And, Yeah, I, I need, like, some more… I… I think time and inputs on how do I frame this, or does it even make sense, and should I just change the name?
So that is, like, where I'm at right now with this proposal, at least.
**Yoshi Yamaguchi** 20:03 Gotcha. So, and then I see a couple of the… I see the… I see the names of a couple… a couple of, observability companies in this document, and then this… So, is… are these… From your research, or you made as a, like… Insert…
**Ayushi Asthana** 20:23 So you…
**Yoshi Yamaguchi** 20:24 Online conversation with the specific stakeholders.
**Ayushi Asthana** 20:28 No, this is just basically, the documentation that exists.
**Yoshi Yamaguchi** 20:34 I see, I see.
**Ayushi Asthana** 20:35 internally, right? So, I don't know if that… did I…
**Yoshi Yamaguchi** 20:40 So you made a, you made the research by yourself?
Based on the…
**Ayushi Asthana** 20:43 Yeah, this is just Public documentation that exists.
**Yoshi Yamaguchi** 20:47 I see. I see, I see.
**Ayushi Asthana** 20:49 So, yeah, I think this is what they do at the moment.
For some sensitivity or categorization use cases, And this is what that… what's possible, if these attributes exist.
So, this was basically the proposal, that what are they doing right now, and what is possible if we have these attributes centrally available through hotel?
So there is some scanning and masking engines that… I think all of the providers have some type of masking engines, that exist.
During the election, with them.
**Yoshi Yamaguchi** 21:35 The basic idea of introducing this attribute is to make Make it easier to identify which data is more sensitive or, like, more, like, critical to… for the, like, security Concerned, and so on.
**Ayushi Asthana** 21:55 Right.
Yes, yes.
**Yoshi Yamaguchi** 21:58 Yeah, okay, yeah, yeah, totally makes sense.
**Ayushi Asthana** 22:02 So yeah, that's… that's where I'm at, and I would like… so there is a few proposals floated right now. One of them was that, because data as an attribute group is getting… A lot of, like, adding pushback.
So, instead of introducing data as an attribute class by itself, we introduce service.data.something.
And so we add data.category, data.sensitory, within service domain.
And… I have no… I mean, I can see it working out, but also, data concerns are not limited to services, so… that is where I was like, do we want to add in service, or… Do you want to explore the option of nailing down data attribute group?
In, like, a better way.
So this is… this is something that's still on the table, so we might just go ahead and add it in development and gather feedback.
Do you… do you have any opinions at the moment, or do you want to, like, look through the proposal and see what you prefer?
**Yoshi Yamaguchi** 23:25 Yeah, so, this data proposal, data attributes group.
**Ayushi Asthana** 23:30 the book.
**Yoshi Yamaguchi** 23:30 Although, sounds good to me.
And then, I think you… I missed a couple of points you discussed. So, are you… are you going to… like… start the new SIG for this data attribute, or data-related attribute, or… I heard a couple of words about, like.
**Ayushi Asthana** 23:51 Boom.
**Yoshi Yamaguchi** 23:52 new SIG or something, but… sorry, I missed the… I missed the conversation.
**Ayushi Asthana** 23:57 No, no, I think, I think the, for now.
until we find out… so right now, most of the use cases that we've proposed are tied closely with whatever we're doing in service, and whatever we are doing in, service and deployments. Yeah. So for now, whatever we do in data attribute group will… we will basically keep this under Service and Deployment SIG, and we don't want another SIG for data explicitly.
But that was, I think, the main concern, that if we do that, can service and deployment SIG handle Everything that comes in? And is that, like, a good idea to do?
**Yoshi Yamaguchi** 24:42 Yeah, because the idea of attributes is really relevant to the security SIG.
Because it handles… and it's because Security 6 handles the security-related topics, and then this is really tied strongly to… The, the, the area.
So, I was, like, wondering if they're interested in looking into this… Proposal or not.
**Ayushi Asthana** 25:11 I have not explored that path yet, and I don't have any qualms against it, to be very honest, if they would want to You know, own data.
As an attribute group, because… I mean, our use cases are also very tied to security at the moment.
And… I mean, I don't have anything against having them take a look at this proposal and see if They're interested.
**Yoshi Yamaguchi** 25:43 Yeah, anyway, yeah, anyway, the use case is really close to their… their interests, and then they may have… Their own opinions on, like, this attribute?
So…
**Ayushi Asthana** 26:03 Okay. Yeah.
Okay, good to have, like, a second set of opinions.
**Yoshi Yamaguchi** 26:09 Yeah, so if you know someone who are in security sake, then just… just give them heads up.
Sounds good to me.
**Ayushi Asthana** 26:19 Okay, okay, makes sense, actually. I can find… Okay. I'll look at the channel and see if I can find somebody.
**Yoshi Yamaguchi** 26:28 Yeah, on my end, I also tap into the product team internally, and then if the security team is interested in this attribute or not, so… Yeah.
**Ayushi Asthana** 26:43 Okay, makes sense, makes sense.
Cool.
**Yoshi Yamaguchi** 26:47 Good.
**Ayushi Asthana** 26:48 Okay, that is all I had for today. I didn't have anything else at the moment.
**Yoshi Yamaguchi** 26:55 Good conversation.
**Ayushi Asthana** 26:56 I'll start a thread for this one, And I'll see you on Slack.
**Yoshi Yamaguchi** 27:02 Yeah, see you there.
Why?
**Ayushi Asthana** 27:06 Thank you so much.
Yeah, huh.
**Yoshi Yamaguchi** 27:07 Have a good day. Bye.
No, no, it was around the opera.
