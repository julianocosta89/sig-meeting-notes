SIG: Service and Deployment SemConv
Date: 2026-06-18
Duration: 120 minutes
============================================================

## Zoom Recording Transcript

**Ayushi Asthana** 08:50 Hey, hijad Marshall.
I don't think anybody else will be joining, it's been 5 minutes.
**Sharmistha Rai** 09:00 I think… I also think nobody will join, it's been 5 minutes. Do you think we should drop off?
**Ayushi Asthana** 09:07 Yes, but while I have you here.
Can we talk about a couple of things that… Yeah, sure.
Yeah, I'll let me just share my screen. So, we had… So last week.
We had the APAC time zone meeting with Yoshi.
So we discussed, like, all of the open things that we have right now.
In Seoul… Basically, for… I think criticality and data specifically, he had some questions.
**Sharmistha Rai** 09:44 Okay.
**Ayushi Asthana** 09:44 4… data, SIG, he wanted to… somebody from… The security space to take a look at this and add any future use cases or future, attributes that they see being added to this group, right? I think we had spoken about, yeah, like, future use cases of this attribute group earlier also.
So, he also had the same question, that maybe somebody from the security space should be involved, and they should basically comment on if they see any, like, more utility out of this attribute group.
So, that is one thing where I might need your help.
To involve… either involve folks from security domain, within GCP or outside of GCP, whatever we decide.
And the second thing was, 4. So, right now, like, criticality exists as an attribute, right, in AppHub.
**Sharmistha Rai** 10:57 Hmm.
**Ayushi Asthana** 10:57 He was interested in knowing more about what AppHub criticality does for customers at this point, and how it's used.
and they wanted that information to comment on.
Basically stabilizing service.criticality. Right now, we've added it in alpha.
**Sharmistha Rai** 11:19 Okay.
**Ayushi Asthana** 11:20 So, these were, like, two things that are open, Yeah, these are the only two things I had. We can, we can discuss about that, we don't have to do it right now, we can discuss about it later also.
But I just wanted to call out that these two things… I need your help and inputs on…
**Sharmistha Rai** 11:39 Got it.
Yeah, I think the AppHub thing is the easier one to do, because we can go through how AppHub uses it and document their use cases.
And signify that this is how we… it's already being used, and we also plan to… make it general purpose for CRM in GCP, so for org folder project in GCP. So that would be the easy part. The second one, where we need somebody from the security side, why did they mention security specifically? Like, what was the reason for that?
**Ayushi Asthana** 12:19 So basically, because the attributes that we are proposing right now, they are data sensitivity and data category.
They have more or less similar use cases, either auditing what type of data is being consumed, or using the sensitivity labels to hide data or reroute data, something like that, right? They're more closely tied to security.
Okay. As use cases. So what… whatever we've mentioned over here in this… this talk, Right? This is… This is more and more closely tied.
Security domain.
**Sharmistha Rai** 13:08 Hmm.
**Ayushi Asthana** 13:12 And… Hello?
Show me time I'm audible?
**Sharmistha Rai** 13:46 Yeah, I can hear you now, it's some network issue.
**Ayushi Asthana** 13:51 Oh, okay, okay.
Yeah, I…
**Sharmistha Rai** 13:53 You were saying that the existing ones are closely related to security. That's where I lost you.
**Ayushi Asthana** 14:01 Okay, yeah, yeah. So, I think it asked why, why they wanted specifically security teams, so that was the.
**Sharmistha Rai** 14:07 Yeah.
**Ayushi Asthana** 14:07 Because the proposal right now is very closely tied to governance use cases. Correct.
So, the curious question here is, will there be more such attributes that will also be closer to security than any other use case? Basically.
**Sharmistha Rai** 14:29 Yeah. All day.
**Ayushi Asthana** 14:30 They also fall in that category.
**Sharmistha Rai** 14:31 Yeah, so one other use case which I… I mean, I cannot promise that it will come or not, but I do see coming from the data teams is malicious content. So, you run a scan of your bucket.
Or your storage resources, and then you identify that, does this resource has any malicious content or not, or it has any malware or not.
So, that could be another tag which can be applied, and that also relates to the security portion of it, right?
That you proactively identify if there is any malicious content, and then you tag it for the resources.
**Ayushi Asthana** 15:16 Mmm… Okay, okay.
I think we'd have to think through… think through the telemetry side of it, but yeah, even… even that seems much more close to security than anything else.
**Sharmistha Rai** 15:29 Yeah, yeah.
**Ayushi Asthana** 15:31 Okay.
**Sharmistha Rai** 15:34 In that case, do they want us to go to the other SIG and get this?
Tell… get this, hotel attribute added there, or they're still okay, but they just want the security Pers… person to come and share their point of view.
**Ayushi Asthana** 15:53 Yeah, so that was… that was the idea that, is the security SIG more equipped to handle this attribute group, and should they own it, or should service and deployment SIG own it?
I think that is the second part of the question. First part still remains, is data attribute group good enough, and very defined enough to be added? And then the second thing is, who should own it?
So the who should own it, I think Yoshi was leaning towards that security SIG is a better place for this attribute group to live in, and to be, like.
Sort of owned by… Instead of service and deployment, because they understand that space better, and what we're doing at elementary in security.
So, that was basically his idea.
So, yeah, there is that. We, we need to, we need to align on, which direction we want to take. I know we had earlier discussed… Yeah.
**Sharmistha Rai** 17:04 Are there other SIGs also? Like, there is one which is… whom we're already talking to, the service and deployment thing. Then there is the security sync. Apart from that, are there other SIGs?
**Ayushi Asthana** 17:18 Oh yeah, there are… there are a lot of SIGs. So I'll just share my calendar for a minute, and you can see. So this… Deals with localization.
**Sharmistha Rai** 17:33 community.
**Ayushi Asthana** 17:33 there is one for Go. Specifically, there is end user, Kubernetes operator.
**Sharmistha Rai** 17:39 There is Scotland.jet.
Okay.
**Ayushi Asthana** 17:45 There is, there is, like, a lot of SIGs, yes.
So, we can… we can find a home for this, no problem, and that's, like, the common thing to do.
But that is, like, a call we need to make. Do we do that, or do we want to redefine what we're doing? I know we had earlier this, like.
toyed with the idea of these being within service, service data.
**Sharmistha Rai** 18:13 Yeah.
**Ayushi Asthana** 18:13 Service data sensitivity.
**Sharmistha Rai** 18:15 Yeah.
**Ayushi Asthana** 18:16 So, if you don't want this ownership, so this is how it will look like, but…
**Sharmistha Rai** 18:23 Yeah.
**Ayushi Asthana** 18:24 If… slash when we want to extend it, we would have to think through those questions, that is this still the right place? Is this still the right thing to do? Because if we decide.
**Sharmistha Rai** 18:36 to grow.
**Ayushi Asthana** 18:36 So this attribute group, those questions will come up.
**Sharmistha Rai** 18:39 Hmm.
Yeah, that is what I'm thinking, right? Because security also, you cannot say that it very closely aligns to security, right?
Ultimately, I just want to categorize my data. If I am tagging my data resources saying that this is finance data, this is PII, this is health.
How does that tie to security? And just tagging the data.
**Ayushi Asthana** 19:07 Mmm, right. I mean, I, I hear you.
The flip side of that is that, what am I doing with that data after I tag it? I mean, we… we are adding semantics, but there is also the whole, like, telemetry part of it. What am I doing after I add that attribute.
**Sharmistha Rai** 19:28 Or rather than… Maybe based on it, I give access to somebody. So, yeah, that access… performing could be tied to security, that I am controlling access, that means I'm controlling the security of the particular… making the objects more secure, let's say.
**Ayushi Asthana** 19:47 Yeah, yeah, yeah, exactly. And then, this is, very specific to… I mean, yeah, I can… I mean, we can make a case either way, very honest.
**Sharmistha Rai** 19:59 Excuse me.
**Ayushi Asthana** 20:00 And that is what we need to decide, what case are we making here, and…
**Sharmistha Rai** 20:06 That's why I was asking, are there more SIGs? Because what if we take to the security SIG, and then they come to us, and then they say, we are thinking that there is this third SIG to which it aligns to better, because then we cannot keep taking this to multiple.
**Ayushi Asthana** 20:23 Yeah, yeah.
**Sharmistha Rai** 20:24 multiple teams.
**Ayushi Asthana** 20:26 Yeah, agreed, agreed. That is the reason, I think, that, we either, like, post it in a wider forum, so there are a few channels in Slack where we can post it.
For, basically for… a review.
And one of them was the working group. I don't know if you were in that meeting.
But there is, like, a general, so these are all of the SIGs, and then there is a working group.
That is just hotel semantics, so it's like a… General, sort of, so this is the group that I was showing. Have you…
**Sharmistha Rai** 21:05 Yeah, like the parent group.
**Ayushi Asthana** 21:07 Yeah, yeah, sort of the parent group for all of the things, where people come when there is, like, they don't know where something is.
**Sharmistha Rai** 21:15 you know.
**Ayushi Asthana** 21:15 Right? So they had also picked up this discussion of where data should live.
Data as an attribute group, and… Their opinion was that, we need to define this attribute group better.
So that, basically, they were just concerned that this might snowball into something much bigger.
**Sharmistha Rai** 21:41 Yeah.
**Ayushi Asthana** 21:41 service and deployment SIG won't be able to handle. So we need to define this attribute group in a way that additions to this attribute group Stay contained, and data does not become, like, a catch-all thing for… you know, stuff. So we either rename this somehow, or we define it in a way so that it does not snowball into something that gets very, very hard to maintain in open source.
**Sharmistha Rai** 22:07 You see, I think we should go with the data.classification group, because even the future case of malicious content that I see coming from storage side, that also is intending to… define or classify the data. So, category is classifying data, sensitivity is classifying data, telling malicious is classifying data, and another thing, or another idea that I heard from, from… GCS side was?
Let's say I have a folder which has 10,000 photos.
I want to be able to know and tag a photo based on what is in the photo. So, I have a photo which is tagged red car, because there is a red car in that photo. That is, again, classifying data, no?
**Ayushi Asthana** 23:01 Like.
**Sharmistha Rai** 23:02 how Google Drive shows me photos of all people if I search by face.
Or if I search by items. So, again, data classification. So, I am thinking we should pitch this thing in the data classification, group?
And then make it very focused, so that this concern at least goes away, that this is too broad, it can become too big, because it's a legit concern from the open telemetry side also, right? They don't want to maintain something which can become anything and everything tomorrow.
**Ayushi Asthana** 23:37 Yeah, yeah, I agree with that, yes.
I think… okay, I… I like… The direction we're headed.
Let me rewrite this. You can also take a look at this and suggest improvements or, you know, rephrasing where we can, you know, pitch it in, like, a more confined way.
**Sharmistha Rai** 24:02 Okay.
**Ayushi Asthana** 24:02 But yeah, I'll rewrite this a little bit.
and pitch it as data classification attribute group instead of just data attribute group. I see that there could be value here there.
**Sharmistha Rai** 24:14 Yeah, so let's rewrite it, and let's, meet, on Wednesday. Thursday morning next week, this meeting will happen, right?
With the APAC reason. Yeah, yeah. So let's… do you think we should, like, let's rewrite it till Wednesday, and then pitch the data classification, group?
in the Thursday meeting, and let's see what the service SIG says. If they still think that the deployment… service and deployment SIG is not the best area for it, then we will pitch it… then we will ask them to help us define the best SIG for it, but let's pivot to data classification, and let's see what we get.
**Ayushi Asthana** 24:55 Makes sense, makes sense. Just FYI, I'm out till Wednesday, but I can work on this tomorrow and send it to you tomorrow anyway, so…
**Sharmistha Rai** 25:03 Okay, yeah, yeah, okay. That, that also works.
**Ayushi Asthana** 25:07 Yeah, and in any case, I think with Yoshi, because the APAC meeting just… Yoshi is the only person that joins outside of, like, all of us, so we can have, like, a conversation with him also.
**Sharmistha Rai** 25:19 That also, okay, yeah, then that's better, then we will have some time to, like, rewrite and review it also. We'll share it with Janvi, ask her opinion, get her to weigh in too, and then, accordingly, we can pitch it.
In the next, this US time zone meeting.
**Ayushi Asthana** 25:39 Makes sense. Cool. I think that works. I don't have anything else for now, though.
**Sharmistha Rai** 25:47 Yeah, nothing else from the audience.
**Ayushi Asthana** 25:51 Okay, cool. I think we can drop. We're the only people here anyway.
**Sharmistha Rai** 25:56 Yeah, okay, good.
**Ayushi Asthana** 25:57 Okay.
**Sharmistha Rai** 25:58 Thank you, Ayush.
**Ayushi Asthana** 25:59 Thank you.
**Sharmistha Rai** 26:00 Bye.
